from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Alumni
from .forms import AlumniRegistrationForm

# Create your views here.

class AlumniRegistrationView(CreateView):
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

    

