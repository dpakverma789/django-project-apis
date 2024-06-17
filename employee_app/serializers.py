from rest_framework import serializers
from . models import Employees


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
    employee_age = serializers.IntegerField()
    employee_salary = serializers.FloatField()

# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employees
#         # fields = ('first_name','last_name')
#         fields = '__all__'

    def create(self, validated_data):
        return Employees.objects.create(**validated_data)