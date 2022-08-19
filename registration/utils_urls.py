from urllib import request, response
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Registration, Student
from django.db.models.functions import TruncWeek
from django.db.models import Count
from django.db.models import Q
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
    data_true_count = []
    data_total_count = []

    queryset = Registration.objects.annotate(week=TruncWeek('created_at')).values('week').annotate(true_count = Count('is_enroll', filter=Q(is_enroll=True))).values('week', 'true_count').annotate(total_count = Count('is_enroll')).values('week', 'true_count', 'total_count').order_by('week')
    for register in queryset:
        labels.append(register['week'].strftime("%a %d/%m"))
        data_true_count.append(register['true_count'])
        data_total_count.append(register['total_count'])
    return render(request, "registration/dashboard.html", {
        'labels': labels,
        'data_true_count': data_true_count,
        'data_total_count': data_total_count,
        })