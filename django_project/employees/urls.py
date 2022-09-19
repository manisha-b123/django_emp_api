from django.urls import path
from employees.views import EmployeesView, EmployeesByIdView, EmployeesByDeptView, FindEmployeesView


urlpatterns = [
    path('employees/', EmployeesView.as_view()),
    path('employees/dept/', EmployeesByDeptView.as_view()),
    path('find/employees/', FindEmployeesView.as_view()),
    path('employees/<int:pk>/', EmployeesByIdView.as_view()),
]