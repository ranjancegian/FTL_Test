from django.http import HttpResponse
from django.conf.urls import url

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.urlpatterns import format_suffix_patterns

from collections import OrderedDict
from .models import Employee

def url_prefix(version):
    return r'v%d/' % version

class DetailListView(APIView):
    required_scopes     = ['read']
    url_path            = 'employee/detail/$'
    view_name           = 'employee_details'
    
    @classmethod
    def urlpatterns(self, version):
        name = 'employee_details'
        prefix = url_prefix(version) + self.url_path
        return [
            url(prefix, self.as_view(), name=name),
        ]

    def get(self, request, format=None):
        data = {"ok": 'true', 'members':[]}
        employees = Employee.objects.all()
        for each_employee in employees:
            emp_data = OrderedDict()
            id_, real_name = each_employee.emp_id, each_employee.real_name
            emp_data['id']=id_
            emp_data['real_name']=real_name
            employee_activity = each_employee.employee.values()
            activity_list = []
            for each in employee_activity:
                tz = each.get('tz','')
                activity_list.append({'start_time':each.get('start_time',''), 'end_time':each.get('end_time','')})
            emp_data['tz']=tz
            emp_data['activity_periods']=activity_list
            data['members'].append(emp_data)
        return Response(data)
