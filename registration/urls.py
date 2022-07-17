from django.urls import path
from . import views
from . import utils_urls

app_name = "registration"

urlpatterns = [
    path("", views.index, name="index"),
    path("register_student/", views.register_student, name="register_student"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("student_details/", views.student_details, name="student_details"),
    path("program_registration/", views.program_registration, name='program_registration'),
    path("program_details/<int:batch_id>", views.program_details, name="program_details"),
    path("program_enrollment/>", views.program_enrollment, name="program_enrollment"),
    path("my_programs/", views.my_programs, name="my_programs"),
    path("edit_form/<str:operation>/<int:form_id>", views.edit_form, name="edit_form"),
    path("send_sms/", views.send_sms_view, name="send_sms_view"),
    path("registrations_list/", utils_urls.registrations_list, name="registrations_list"),
    path("download_registration_csv/", utils_urls.download_registration_csv, name="download_registration_csv"),
    path("download_students_csv/", utils_urls.download_students_csv, name="download_students_csv"),
]