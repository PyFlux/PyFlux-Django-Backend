from rest_framework import serializers
from .models import *

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = "__all__"


class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = "__all__"


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = "__all__"


class LeaveStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveStructure
        fields = "__all__"


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = "__all__"


class LoanTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanType
        fields = "__all__"


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = "__all__"


class ShiftAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftAllocation
        fields = "__all__"


class WeekOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekOff
        fields = "__all__"


class LeaveApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveApplication
        fields = "__all__"

class LeaveReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReporting
        fields = "__all__"
