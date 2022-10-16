# TODO: Localization to english and then Sudanese Arabic
# TODO: security for phone number and transaction IDs


from datetime import datetime
from urllib import response
from xml.dom.domreg import registered
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, request
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

import re
from datetime import datetime


from .models import *
from .forms import *
from .sms import send_sms
from .utils import *
# import requests as req

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("registration:index"))

    if request.method == "GET":
        quote = get_quote()

        return render(request, "registration/login.html", {
            "form": register_login_form(),
            "progress": 0,
            "quote": quote,
        })
    elif request.method == "POST":
        form = register_login_form(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["username"]
            pin = form.cleaned_data["password"]
            phone_number = f"249{phone_number[-9:]}"
            if len(phone_number) < 10 or len(pin) != 1 or not pin.isnumeric():
                return render(request, "registration/login_student.html", {
                    "form": form,
                    "error_message": "الرجاء إدخال معلومات صحيحة حسب وصف كل حقل"
                })
            else:
                student = authenticate(
                    request, username=phone_number, password=pin)
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


@login_required(redirect_field_name=None)
def index(request):
    if not request.user.is_complete:
        return HttpResponseRedirect(reverse("registration:student_details"))

    request.session["programs_count"] = Registration.objects.filter(
        student=request.user, is_enroll=False).count()
    return render(request, "registration/landing.html", {
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
            quote = get_quote()
            return render(request, "registration/register.html", {
                "form": register_login_form(),
                "progress": 1,
                "quote": quote,
            })
    # if the request == POST then check the information
    elif request.method == "POST":
        new_student = register_login_form(request.POST)
        if new_student.is_valid():
            phone_number = new_student.cleaned_data["username"]
            pin = new_student.cleaned_data["password"]

            # check if the phone number length is more than or equal to 10, if yes, then slice the last 9 numbers, if no send and error
            # check if the pin number isn't numaric or isn't a one number.
            if len(pin) != 1 or not pin.isnumeric():
                return render(request, "registration/register.html", {
                    "form": new_student,
                    "error_message": "الرجاء إدخال معلومات صحيحة حسب وصف كل حقل",
                    "progress": 1,
                })
            if len(phone_number) < 10 or len(pin) != 1 or not pin.isnumeric():
                return render(request, "registration/register.html", {
                    "form": new_student,
                    "error_message": "الرجاء إدخال معلومات صحيحة حسب وصف كل حقل",
                    "progress": 1,
                })
            phone_number = f"249{phone_number[-9:]}"
            # try to save the new students to the database
            try:
                student = Student.objects.create_user(
                    username=phone_number, password=pin, is_complete=False)
                student.save()

            except Exception as e:
                print(e)
                return render(request, "registration/register.html", {
                    "form": new_student,
                    "error_message": " رقم التلفون موجود بالفعل إذهب لصفحة تسجيل الدخول"
                })
            login(request, student)

            # We're not sending SMS to the customer upon registration because there are some user who didn't finished their details, so we don't know 
            # Send the SMS to the customers when registered
            # send_sms(phone_number=phone_number, sms_to_send="registration_sms")

            return HttpResponseRedirect(reverse("registration:index"))
        else:
            return render(request, "registration/register.html", {
                "form": new_student,
            })


@login_required(redirect_field_name=None)
def student_details(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            student_details_form = student_details_from()

            user_details = Student.objects.filter(pk=request.user.id)

            student_details_form.initial["first_name"] = user_details[0].first_name
            student_details_form.initial["father_name"] = user_details[0].father_name
            student_details_form.initial["email"] = user_details[0].email
            student_details_form.initial["gender"] = user_details[0].gender
            student_details_form.initial["birthday"] = user_details[0].birthday
            student_details_form.initial["occupation"] = user_details[0].occupation
            student_details_form.initial["university"] = user_details[0].university
            student_details_form.initial["specialization"] = user_details[0].specialization
            student_details_form.initial["state"] = user_details[0].state
            student_details_form.initial["address"] = user_details[0].address

            return render(request, "registration/student_details.html", {
                "form": student_details_form,
            })

        else:
            return render(request, "registration/student_details.html", {
                "form": student_details_from(),
                "progress": 20,
            })
    elif request.method == "POST":
        new_student_details = student_details_from(request.POST)
        if new_student_details.is_valid():
            first_name = new_student_details.cleaned_data["first_name"]
            father_name = new_student_details.cleaned_data["father_name"]
            email = new_student_details.cleaned_data["email"]
            gender = new_student_details.cleaned_data["gender"]
            birthday = new_student_details.cleaned_data["birthday"]
            occupation = new_student_details.cleaned_data["occupation"]
            university = new_student_details.cleaned_data["university"]
            specialization = new_student_details.cleaned_data["specialization"]
            state = new_student_details.cleaned_data["state"]
            address = new_student_details.cleaned_data["address"]

            try:
                Student.objects.filter(pk=request.user.pk).update(first_name=first_name, father_name=father_name, email=email, gender=gender,
                                                                  birthday=birthday, occupation=occupation, university=university, specialization=specialization, state=state, address=address)
                Student.objects.filter(pk=request.user.pk).update(is_complete=True)
            except:
                return render(request, "registration/student_details.html", {
                    "form": new_student_details,
                    "error_message": "للأسف واجهتنا مشكلة أثناء حفظ بياناتك الرجاء المحاولة مرة أخرى",
                })

            # sending the SMS when recieving the data
            # send_sms(phone_number=request.user.username, sms_to_send="details_completed", name=first_name)
            return HttpResponseRedirect(reverse("registration:program_registration"))
        else:
            return render(request, "registration/student_details.html", {
                "form": new_student_details,
                "error_message": "للأسف واجهتنا مشكلة أثناء حفظ بياناتك الرجاء المحاولة مرة أخرى",
            })

@login_required(redirect_field_name=None)
def landing_view(request):
    return render(request, "registration/landing.html", {
            })

@login_required(redirect_field_name=None)
def program_registration(request):

    quote = get_quote()

    if request.method == "GET":

        

        all_batches = Batch.objects.filter(ending_at__gte=datetime.today()).order_by("id")

        basic_edition_details = re.split('\n', all_batches[0].program.basic_edition_details)
        golden_edition_details = re.split('\n', all_batches[0].program.golden_edition_details)

        return render(request, "registration/program_choice.html", {
            "batches": all_batches,
            "progress": 40, 
            "quote": quote,
            "basic_edition_details": basic_edition_details,
            "golden_edition_details": golden_edition_details,
        })
                 

@login_required(redirect_field_name=None)
def program_details(request, batch_id):
    quote = get_quote()
    if request.method == "GET":
            batch = Batch.objects.get(id=batch_id)

            basic_edition_details = re.split('\n', batch.program.basic_edition_details)
            golden_edition_details = re.split('\n', batch.program.golden_edition_details)
            curriculum   = re.split('\n',batch.program.curriculum)
            
            

            registrated = Registration.objects.filter(student=request.user, batch=batch, is_enroll=False).first()
            
            if registrated == None:
                try:
                    registration = Registration.objects.create(student=request.user, program=Program.objects.get(name_arabic=getattr(batch, "program")),batch= batch, is_register=True, is_enroll=False)
                    request.session['registration_id'] = registration.id
                except Exception as e:
                    print(e)
                    return HttpResponseRedirect(reverse("registration:index"))
            else:
                request.session['registration_id'] = registrated.id
                
            
            return render(request, "registration/program_details.html", {
                "batch": batch,
                "progress": 60,
                "quote": quote,
                "basic_edition_details": basic_edition_details,
                "golden_edition_details": golden_edition_details,
                "curriculum": curriculum
            })
            


            return render(request, "registration/program_details.html", {
            "batch": batch,
            "progress": 60,
            "quote": quote,
        })


@login_required(redirect_field_name=None)
def program_enrollment(request, package):
    quote = get_quote()
    if request.method == "GET":

        try:
            registrated = Registration.objects.get(pk=request.session['registration_id'])
            registrated.package = package
            if package == 'golden':
                registrated.price = registrated.batch.golden_edition_price
            elif package == 'basic':
                registrated.price = registrated.batch.basic_edition_price
            else:
                registrated.price = 0
            registrated.save()
        except Exception as e:
            print(e)
            return HttpResponseRedirect(reverse("registration:program_registration"))

        if registrated.is_register == False:
            return HttpResponseRedirect(reverse("registration:program_registration"))
        else:
            enrollment_form = new_enrollment_from()
            enrollment_form.initial["transaction_id"] = registrated.transaction_id
            enrollment_form.initial["confirm_transaction"] = registrated.transaction_id
            enrollment_form.initial["reach_channels"] = registrated.reach_channels

            #get the batch to update the prices accordingly in the html
            batch = Batch.objects.get(pk=registrated.batch.id)

            #get the quotation using get_quote function from the utils file
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
                send_sms(request.user.username, sms_to_send="program_enrollment_sms", program=registration_form.program.name_arabic)

                return render(request, "registration/successful.html", {
                    "progress": 100,
                })
            else:
                return render(request, "registration/program_enrollment.html", {
                    "error_message": "هنالك مشكلة في رقم العملية الذي أدخلته",
                    "form": new_enrollment,
                    "progress": 60
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