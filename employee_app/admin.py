from django.contrib import admin
from . models import Employees
# Register your models here.

# admin.site.register(Employees)

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'employee_age','employee_salary']
    search_fields = ("first_name",)
    list_filter = ("employee_age",)
    ordering = ("first_name",) # add "-" for descending
    list_display_links = ("first_name", "last_name")
    list_editable = ("employee_salary",) # field should be present in list_display
    readonly_fields = ("first_name", "last_name")
    # exclude = ("employee_salary",) # this hide the field from list view
    fieldsets = (
        ("Basic Info", {
            "fields": ("first_name", "last_name")
        }),
        ("Extra Info", {
            "fields": ('employee_age','employee_salary')
        }),
    )  # make section in form view
    list_per_page = 10

    actions = ["reset_salary"]     # label for Custom bulk actions.
    def reset_salary(self, request, queryset):
        """
        this is what Custom bulk actions do
        :param request:
        :param queryset:
        :return:
        """
        queryset.update(employee_salary=0)
