from django.contrib import admin
from .models import *

@admin.register(JobberUser)
class JobberUserAdmin(admin.ModelAdmin):
    list_display = ['user','name', 'email','phone','address', 'province']
    ordering = ['user','name','email','phone','address','province']
    search_fields = ['name','email','province__province']

@admin.register(EmployerUser)
class EmployerUserAdmin(admin.ModelAdmin):
    list_display = ['user','name','emp_name' ,'email','phone','address', 'province']
    ordering = ['user','name','emp_name','email','phone','address','province']
    search_fields = ['user','name','emp_name','email','phone','address','province__province']

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ['user','name','email']
    ordering = ['user','name','email']
    search_fields = ['user','name','email']

@admin.register(JobberCheck)
class JobberCheckAdmin(admin.ModelAdmin):
    list_display = ['jobber','gender','identity_pic','check_jobber']
    ordering = ['jobber','gender','identity_pic']
    search_fields = ['jobber']

@admin.register(EmployerCheck)
class EmployerCheckAdmin(admin.ModelAdmin):
    list_display = ['employer','identity_pic','check_emp']
    ordering = ['employer','identity_pic','check_emp']
    search_fields = ['employer']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name','phone','gender','emp_name','province','pay']
    ordering = ['name','phone','gender','emp_name','province','pay']
    search_fields = ['name','emp_name']

@admin.register(ApplyJob)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ['job','jobber','emp_name','apply_date','check_apply']
    ordering = ['job','jobber','emp_name','apply_date','check_apply']
    search_fields = ['job','jobber','emp_name']

@admin.register(JobberComplain)
class JobberAdmin(admin.ModelAdmin):
    list_display = ['job','jobber','emp_name','subject','complain_date','status']
    ordering = ['job','jobber','emp_name','subject','complain_date','status']
    search_fields = ['job','jobber','emp_name','subject']

@admin.register(EmployerComplain)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['job','jobber','emp_name','subject','complain_date','status']
    ordering = ['job','jobber','emp_name','subject','complain_date','status']
    search_fields = ['job','jobber','emp_name','subject']