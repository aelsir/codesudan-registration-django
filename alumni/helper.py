from django.http import HttpResponseRedirect
from core.models import Registration
from django.urls import reverse

# this function is going to change is_complete in the core form to true
def change_is_complete(request, form_id):
    Registration.objects.filter(pk = form_id).update(is_complete=True)
    return HttpResponseRedirect(reverse('alumni:core'))