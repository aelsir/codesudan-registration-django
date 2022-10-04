from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta
from . models import *

# Create your views here.

def index(request):
    status = BankakStatus.objects.first()
    status = status.current_status
    
    return render(request, "bankak/index.html", {
        "status": status
    })


def update_status():
    now = datetime.now()
    delta = timedelta(minutes=30)

    #input_status = BankakInput.objects.filter(time__gte(now-delta))

    if now.minute%15:
        pass

def post_status():
    pass