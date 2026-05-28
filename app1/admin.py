from django.contrib import admin

from app1.models import employee

class employee_admin(admin.ModelAdmin):
    list_display = ['Employee_name','Employee_id','Employee_email','Employee_salary']
    ordering = ['Employee_id']
admin.site.register(employee,employee_admin)
