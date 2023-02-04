from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['province']
    ordering = ['province']
    search_fields = ['province']

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['gender']
    ordering = ['gender']
    search_fields = ['gender']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['education']
    ordering = ['education']
    search_fields = ['education']

@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = ['pay']
    ordering = ['pay']
    search_fields = ['pay']

@admin.register(JobberSubjectComplain)
class JobberSubjectComplainAdmin(admin.ModelAdmin):
    list_display = ['subject']
    ordering = ['subject']
    search_fields = ['subject']

@admin.register(EmployerSubjectComplain)
class JobberSubjectComplainAdmin(admin.ModelAdmin):
    list_display = ['subject']
    ordering = ['subject']
    search_fields = ['subject']



