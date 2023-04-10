from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Alumni
from .forms import AlumniRegistrationForm
from core.models import Registration

# Create your views here.
@login_required
def alumni_registration(request):
    if request.method == 'GET':
        # get all of the student registrations programmes 
        registrations = request.user.my_registrations.all().filter(is_enroll=True)
        if not registrations:
             return HttpResponseRedirect(reverse('coreregistration:index'))
        return render(request, 'registration.html', {
            'registrations': registrations,
            'alumni_form': AlumniRegistrationForm()
        })
    elif request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)
        if form.is_valid():
            form.instance.alumni = request.user
            form.save()
            return HttpResponseRedirect(reverse('alumni:list'))
    

class AlumniDetailView(LoginRequiredMixin, ListView):
    model = Alumni
    context_object_name = 'alumnis'
    template_name = 'list.html'

    

