from shared.views import CURDViewSet
from hr.models import *
# from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response


class checkEmployeeCodeTaken(APIView):
    """
    * Check Employee code is Taken
    """
    def get(self, request):        
        empcode = request.GET['empcode']        

        # On EDIT
        employee = request.GET.get('employeeid','')
        if employee:
            # on employee edit
            emp = Employee.objects.get(id = employee)

            # if employee code = given code
            # then not taken
            if emp.emp_code == empcode:
                return Response({'empcodeTaken': False})

        # on Add
        if Employee.objects.filter(emp_code = empcode):
            # if empcode already exists in db
            return Response({'empcodeTaken': True})
        return Response({'empcodeTaken': False})
