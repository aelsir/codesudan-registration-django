from django.urls import path
from . import views
from . import utils_urls

app_name = "registration"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
         

    path("student_details/<int:pk>/", views.StudentDetailView.as_view(), name="student_details"),
         

    path("landing/", views.landing_view, name="landing"),
    path("program_registration/", views.program_registration, name='program_registration'),
    path("program_details/<int:batch_id>", views.program_details, name="program_details"),
    path("program_enrollment/<int:batch_id>/<str:package>", views.program_enrollment, name="program_enrollment"),
    path("my_programs/", views.my_programs, name="my_programs"),
    path("edit_form/<str:operation>/<int:form_id>", views.edit_form, name="edit_form"),
    path("send_sms/", views.send_sms_view, name="send_sms_view"),
    path("registrations_list/", utils_urls.registrations_list, name="registrations_list"),
    path("download_registration_csv/", utils_urls.download_registration_csv, name="download_registration_csv"),
    path("download_students_csv/", utils_urls.download_students_csv, name="download_students_csv"),
    path("dashboard/", utils_urls.dashboard, name="dashboard"),
    path("demo/", utils_urls.demo, name="demo")
]