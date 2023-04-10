from urllib import request, response
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Registration, Student
from django.db.models.functions import TruncWeek
from django.db.models import Count
from django.db.models import Q
from django.http import HttpResponse
from .utils import *


# show all of the core, to easily contact them on whatsapp by creating custom whatsapp link
@staff_member_required
def registrations_list(request):
    if request.method == "GET":
        all_registrations = Registration.objects.all().order_by("-created_at")
        return render(request, "registration/registrations_list.html", {
            "all_registrations": all_registrations,
        })

# download the students core list in a CSV
@staff_member_required
def download_registration_csv(request):
    data = download_csv(request, Registration.objects.all())
    response = HttpResponse(data, content_type='text/csv; charset=utf-8-sig')
    return response

@staff_member_required
def download_students_csv(request):
    data = download_csv(request, Student.objects.all())
    response = HttpResponse(data, content_type='text/csv; charset=utf-8-sig')
    return response

@staff_member_required
def dashboard(request):
    labels = []
    data_true_count = []
    data_total_count = []

    queryset = Registration.objects.annotate(week=TruncWeek('created_at')).values('week').annotate(true_count = Count('is_enroll', filter=Q(is_enroll=True))).values('week', 'true_count').annotate(total_count = Count('is_enroll')).values('week', 'true_count', 'total_count').order_by('week')
    for register in queryset:
        labels.append(register['week'].strftime("%a %d/%m"))
        data_true_count.append(register['true_count'])
        data_total_count.append(register['total_count'])

    # register details to do analysis on people who registerd

    queryset_registration = Registration.objects.select_related('student').filter(is_enroll=True)
    gender = []
    occupation = []
    for i in queryset_registration:
        gender.append(i.student.gender)
        occupation.append(i.student.occupation)
    gender_dict = dict((x, gender.count(x)) for x in set(gender))
    occupation_dict = dict((x, occupation.count(x)) for x in set(occupation))

    gender_lable = list(gender_dict.keys())
    gender_date = list(gender_dict.values())

    labels_occupation = list(occupation_dict.keys())
    data_occupation = list(occupation_dict.values())


    return render(request, "core/dashboard.html", {
        'labels': labels,
        'data_true_count': data_true_count,
        'data_total_count': data_total_count,
        'gender_lable': gender_lable,
        'gender_data': gender_date,
        'labels_occupation': labels_occupation,
        'data_occupation': data_occupation,
        'core': queryset,
        })


def demo(request):
    
    queryset = Registration.objects.raw('''
    select to_char(created_at, 'yyyy-MM-dd') as date, count(is_enroll = true or null) as enrolled, count(id) as total from registration_registration
    group by date
    order by date desc;
    ''')
    for i in queryset:
        print(i.enrolled)

    return HttpResponse("yoo")

