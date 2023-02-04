from django.urls import path
from .views import AlumniRegistrationView, AlumniDetailView

app_name = 'alumni'

urlpatterns = [
    path('', AlumniRegistrationView.as_view(), name='registration'),
    path('list/', AlumniDetailView.as_view(), name='list')
]
