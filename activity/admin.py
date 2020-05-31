from django.contrib.admin import register, ModelAdmin
from .models import Employee, EmployeeActivity

@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ('emp_id', 'real_name','active')
    list_filter  = ('active',)

@register(EmployeeActivity)
class EmployeeActivityAdmin(ModelAdmin):
    list_display = ('employee', 'tz', 'start_time' ,'end_time')


