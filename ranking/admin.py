from django.contrib import admin
from .models import Developer

# Register your models here.

@admin.register(Developer)
class DeveoperAdmin(admin.ModelAdmin):
    list_display = ('name_arabic', 'rank')
    ordering = ('-rank',)
    search_fields = ['name_arabic', 'name_english', 'rank']


