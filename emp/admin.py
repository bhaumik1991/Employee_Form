from django.contrib import admin
from emp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name','email', 'gender', 'image', 'status')

admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
