# TODO: Localization to english and then Sudanese Arabic
# TODO: security for phone number and transaction IDs


from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, resolve_url
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

import re
from datetime import datetime


from .models import *
from .forms import *
from .sms import send_sms
from .utils import *
from .helper import valid_phone_number, valid_pin

# SMTP import to send an email
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Class-base views import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


@login_required(redirect_field_name=None)
def index(request):
    # if the user didn't complete his info, you redirect him to complete it.
    if not request.user.is_complete:
        return HttpResponseRedirect(resolve_url("registration:student_details", pk=request.user.id))
    return render(request, "registration/landing.html")

class StudentDetailView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = student_details_from
    template_name = "registration/student_details.html"
    success_url = reverse_lazy('registration:program_registration')

    def form_valid(self, form):
        # If the form is valid, save the associated model.

        # Before saving the form change the is_complete attribute to True
        self.object.is_complete = True
        self.object = form.save()
        return super().form_valid(form)
    

def login_view(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("registration:index"))

    if request.method == "GET":

        # if the method is get render the login template
        return render(request, "registration/login.html", {
            "form": register_login_form(),
        })
    
    elif request.method == "POST":
        form = register_login_form(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["username"]
            pin = form.cleaned_data["password"]
            phone_number = f"249{phone_number[-9:]}"
            if not valid_phone_number(phone_number) or not valid_pin(pin):
                return render(request, "registration/login_student.html", {
                    "form": form,
                    "error_message": "الرجاء إدخال معلومات صحيحة حسب وصف كل حقل"
                })
            else:
                student = authenticate(request, username=phone_number, password=pin)
                if student is not None:
                    login(request, student)
                    return HttpResponseRedirect(reverse("registration:index"))
                else:
                    return render(request, "registration/login.html", {
                        "form": form,
                        "error_message": "هذا الرقم غير مسجل، الرجاء التسجيل"
                    })
        else:
            return render(request, "registration/login.html", {
                "form": form,
                "error_message": "الرجاء المحاولة مرة أخرى"
            })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("registration:login"))


def register(request):
    # if the request == GET then display the new registration form

    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("registration:index"))
        else:
            return render(request, "registration/register.html", {
                "form": register_login_form(),
            })
    # if the request == POST then check the information
    elif request.method == "POST":
        new_student = register_login_form(request.POST)
        if new_student.is_valid():
            phone_number = new_student.cleaned_data["username"]
            pin = new_student.cleaned_data["password"]
            phone_number = f"249{phone_number[-9:]}"

            # check if the phone number length is more than or equal to 10, if yes, then slice the last 9 numbers, if no send and error
            # check if the pin number isn't numaric or isn't a one number.
            if not valid_phone_number(phone_number) or not valid_pin(pin):
                return render(request, "registration/register.html", {
                    "form": new_student,
                    "error_message": "الرجاء إدخال معلومات صحيحة حسب وصف كل حقل",
                })
            
            # try to save the new students to the database
            try:
                student = Student.objects.create_user(username=phone_number, password=pin, is_complete=False)
                student.save()
            except Exception as e:
                return render(request, "registration/register.html", {
                    "form": new_student,
                    "error_message": " رقم التلفون موجود بالفعل إذهب لصفحة تسجيل الدخول"
                })
            login(request, student)
            return HttpResponseRedirect(reverse("registration:index"))
        
        else:
            return render(request, "registration/register.html", {
                "form": new_student,
            })


@login_required(redirect_field_name=None)
def landing_view(request):
    return render(request, "registration/landing.html", {
            })

@login_required(redirect_field_name=None)
def program_registration(request):
    if request.method == "GET":
        
        batches = Batch.objects.filter(ending_at__gte=datetime.today()).order_by("id")

        if len(batches) <= 0:
            batches = None
        
        

        return render(request, "registration/program_choice.html", {
            "batches": batches,
        })
                 

@login_required(redirect_field_name=None)
def program_details(request, batch_id):
    if request.method == "GET":
            batch = Batch.objects.get(id=batch_id)

            basic_edition_details = re.split('\n', batch.program.basic_edition_details)
            golden_edition_details = re.split('\n', batch.program.golden_edition_details)
            curriculum   = re.split('\n',batch.program.curriculum)
                
                
            return render(request, "registration/program_details.html", {
                "batch": batch,
                "basic_edition_details": basic_edition_details,
                "golden_edition_details": golden_edition_details,
                "curriculum": curriculum
            })


@login_required(redirect_field_name=None)
def program_enrollment(request, batch_id, package):
    quote = get_quote()
    if request.method == "GET":
        batch = Batch.objects.get(id=batch_id)
        registration = Registration.objects.filter(student=request.user, batch=batch, is_enroll=False).first()

        if registration == None:
            try:
                registration = Registration.objects.create(student=request.user, program=batch.program,batch= batch, is_register=True, is_enroll=False)
            except Exception as e:
                print(e)
                return HttpResponseRedirect(reverse("registration:program_registration"))

        registration.package = package
        if package == 'golden':
            registration.price = batch.golden_edition_price
        elif package == 'basic':
            registration.price = batch.basic_edition_price
        else:
            registration.price = 0
        registration.save()
        request.session['registration_id'] = registration.id


        # check if the price is zero automaticlly register the student and render the success page
        if registration.price == 0:
            registration.transaction_id = 123456789
            registration.is_enroll = True
            registration.created_at = datetime.now()
            registration.reach_channels = 'Unknown'
            registration.save()

            # send enrollment SMS
            send_sms(request.user.username, sms_to_send="program_enrollment_sms", program=batch.program.name_arabic)

            #render the successful page
            return render(request, "registration/successful.html", {
                    "progress": 100,
                    "batch": batch
                })


        if registration.is_register == False:
            return HttpResponseRedirect(reverse("registration:program_registration"))
        else:
            enrollment_form = new_enrollment_from()
            enrollment_form.initial["transaction_id"] = registration.transaction_id
            enrollment_form.initial["confirm_transaction"] = registration.transaction_id
            enrollment_form.initial["reach_channels"] = registration.reach_channels


            return render(request, "registration/program_enrollment.html", {
                "form": enrollment_form,
                "progress": 80,
                "quote": quote,
                "package": package,
                "batch": batch
            })
            
    elif request.method == "POST":
        new_enrollment = new_enrollment_from(request.POST)
        if new_enrollment.is_valid():
            transaction_id = int(new_enrollment.cleaned_data["transaction_id"])
            confirm_transaction = int(new_enrollment.cleaned_data["confirm_transaction"])
            reach_channels = str(new_enrollment.cleaned_data["reach_channels"])
            if transaction_id == confirm_transaction and transaction_id > 100000:
                try:
                    Registration.objects.filter(pk=request.session.get("registration_id")).update(transaction_id=transaction_id, is_enroll=True, created_at=datetime.now(), reach_channels=reach_channels)
                    registration_form = Registration.objects.get(pk=request.session.get("registration_id"))
                    
                except:
                    return render(request, "registration/program_enrollment.html", {
                        "form": new_enrollment,
                        "progress": 60
                    })
                print(registration_form)
                #send and SMS after enrollment
                # send_sms(request.user.username, sms_to_send="program_enrollment_sms", program=registration_form.program.name_arabic)
                batch = Batch.objects.get(pk=batch_id)
                try:
                    template = render_to_string('registration/email_success.html', {
                        'name': registration_form.student.first_name,
                        'program': registration_form.program.name_arabic,
                    })
                    # send SMTP email to the customer
                    email = EmailMessage(
                        f'إكمال تسجيلك لبرنامج {registration_form.program.name_arabic}',
                        template,
                        settings.EMAIL_HOST_USER,
                        [registration_form.student.email],
                    )
                    email.fail_silently = False
                    email.content_subtype = 'html'
                    email.send()
                except Exception as e:
                    print("The message isn't send XXX")

                return render(request, "registration/successful.html", {
                    "progress": 100,
                    'batch': batch,
                })
            else:
                return render(request, "registration/program_enrollment.html", {
                    "error_message": "هنالك مشكلة في رقم العملية الذي أدخلته",
                    "form": new_enrollment,
                })
        else:
            return render(request, "registration/program_enrollment.html", {
                "form": new_enrollment
            })


# Features


@login_required(redirect_field_name=None)
def my_programs(request):
    if request.method == "GET":
        all_programs = Registration.objects.filter(
            student=request.user,).order_by("-created_at")
        return render(request, "registration/my_programs.html", {
            "all_programs": all_programs,
        })


@login_required(redirect_field_name=None)
def edit_form(request, operation, form_id):
    if operation == "edit":
        request.session["form_id"] = form_id
        return HttpResponseRedirect(reverse("registration:program_enrollment"))
    elif operation == "delete":
        Registration.objects.filter(pk=form_id).delete()
        request.session["programs_count"] = Registration.objects.filter(
            student=request.user, is_enroll=False).count()
        return HttpResponseRedirect(reverse("registration:my_programs"))


@login_required(redirect_field_name=None)
def send_sms_view(request):
    
    send_sms("249921093899", sms_to_send="details_completed", name="احمد")
    
    return HttpResponse("Hwlloe")