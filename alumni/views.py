from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Alumni
from .forms import AlumniRegistrationForm
from registration.models import Registration

# Create your views here.

def alumni_registration(request):
    if request.method == 'GET':
        # get all of the student registrations programmes 
        registrations = request.user.my_registrations.all().filter(is_enroll=True)
        if not registrations:
             return HttpResponseRedirect(reverse('registration:index'))
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



class AlumniRegistrationView(LoginRequiredMixin, CreateView):
    model = Alumni
    form_class = AlumniRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('registration:index')

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.alumni = self.request.user
        return super().form_valid(form)
    

class AlumniDetailView(ListView):
    model = Alumni
    context_object_name = 'alumnis'
    template_name = 'list.html'

    

