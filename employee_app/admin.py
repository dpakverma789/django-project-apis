from django.contrib import admin
from . models import Employees
# Register your models here.

admin.site.register(Employees)

# @admin.register(Employees)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'employee_age', 'employee_salary']
