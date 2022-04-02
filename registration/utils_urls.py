from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Registration
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