from django.contrib import admin
from .models import Alumni

# Register your models here.
@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    pass
