from django.urls import path
from .views import index

app_name = 'alumni'

urlpatterns = [
    path('', index, name='index')
]
