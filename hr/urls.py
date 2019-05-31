from rest_framework import routers
from hr.views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'designation', designation.DesignationListAPIView)
router.register(r'employee', employee_views.EmployeeListAPIView)
router.register(r'employeemaster', employee_views.EmployeeMasterListAPIView)
router.register(r'employeecategory', emp_category.EmployeeCategoryListAPIView)
router.register(r'holiday', holiday.HolidayListAPIView)
router.register(r'leavestructure', leave_structure.LeaveStructureListAPIView)

router.register(r'leavetype', leave_type.LeaveTypeListAPIView)
router.register(r'loantype', loan_type.LoanTypeListAPIView)
router.register(r'shift', shift.ShiftListAPIView)
router.register(r'shiftallocation', shift_allocation.ShiftAllocationListAPIView)
router.register(r'weekoff', week_off.WeekOffListAPIView)
router.register(r'leaveapplication', leave_application.LeaveApplicationListAPIView)
router.register(r'leavereporting', leave_reporting.LeaveReportingListAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('empoyeemasterdata/', employee_views.getEmployeeMaster.as_view()),
    path('getuserfrmteachers/', get_teachers.GetUser_Teachers.as_view()),
    path('checkEmployeeCodeTaken/', check_employee_code.checkEmployeeCodeTaken.as_view()),
    path('getteachername/',employee_views.GetTeachername.as_view()),
    path('current_user/',current_user.Get_Current_user.as_view()),
    path('users/',current_user.Get_users.as_view()),
    path('get_roles/',get_roles.GetRoles.as_view()),
    path('get_teacherdetails/',get_teacherdetails.Get_TeachersDetails.as_view()),
    path('current_username/',current_user.Get_Current_username.as_view()),
    path('csvfileexport/', csvexport.CsvFileExport.as_view()),
]
