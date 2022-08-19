from urllib import request, response
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Registration, Student
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.http import HttpResponse
from .utils import *


# show all of the registration, to easily contact them on whatsapp by creating custom whatsapp link
@staff_member_required
def registrations_list(request):
    if request.method == "GET":
        all_registrations = Registration.objects.all().order_by("-created_at")
        return render(request, "registration/registrations_list.html", {
            "all_registrations": all_registrations,
        })


# download the students registration list in a CSV
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
    data = []

    queryset = Registration.objects.annotate(month=TruncMonth('created_at')).filter(is_enroll=True).values('month').annotate(c = Count('is_enroll')).values('month', 'c')
    for register in queryset:
        labels.append(register['month'].strftime('%B'))
        data.append(register['c'])
    return render(request, "registration/dashboard.html", {
        'labels': labels,
        'data': data,
        })