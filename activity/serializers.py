from rest_framework import serializers

from .models import EmployeeActivity


class EmployeeDetailListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeActivity
        fields = ['employee', 'tz', 'start_time', 'end_time']

