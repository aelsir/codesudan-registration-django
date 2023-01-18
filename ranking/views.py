from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Developer


# Create your views here.

class DevelopersListView(LoginRequiredMixin, ListView):
    model = Developer
    template_name = 'developers_list.html'
    context_object_name = 'developers'
    ordering = 'rank'
