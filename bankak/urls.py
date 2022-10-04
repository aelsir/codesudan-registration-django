from django.urls import path
from . import views

app_name = "bankak"

urlpatterns = [
    path("", views.index, name="index"),
]