from django.contrib import admin
from .models import *

# Register your models here.

def get_phone_number(obj):
    return(f"{obj.student.username}")
def get_batch_number(obj):
    return(f"{obj.batch.number}")
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', get_phone_number, 'program', get_batch_number, 'created_at', 'package', 'is_enroll', 'transaction_id', 'is_texted')
    list_filter = ('created_at', 'is_enroll', 'program')

def full_name(obj):
    return(f"{obj.first_name} {obj.father_name}")
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', full_name, 'email', 'university', 'is_complete')


class BatchAdmin(admin.ModelAdmin):
    list_display= ('program', 'number', 'ending_at')
 

admin.site.register(Student, StudentAdmin)
admin.site.register(Track)
admin.site.register(Program)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(CodeSudanQuote)
