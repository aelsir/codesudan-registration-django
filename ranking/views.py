from django.shortcuts import render
from django.views.generic import ListView

from .models import Developer


# Create your views here.

class DevelopersListView(ListView):
    model = Developer
    template_name = 'developers_list.html'
    context_object_name = 'developers'
    ordering = '-contribs'
