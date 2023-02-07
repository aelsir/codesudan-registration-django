from django.urls import path
from .views import AlumniRegistrationView, AlumniDetailView, alumni_registration
from .helper import change_is_complete

app_name = 'alumni'

urlpatterns = [
    path('', alumni_registration, name='registration'),
    path('change_is_complete/<int:form_id>', change_is_complete, name='change_is_complete'),
    path('list/', AlumniDetailView.as_view(), name='list')
]
