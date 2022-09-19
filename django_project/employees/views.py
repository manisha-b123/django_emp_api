from rest_framework.generics import ListCreateAPIView, ListAPIView
from employees.models import EmployeesModel
from employees.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import filters


# Create your views here.
class EmployeesView(ListCreateAPIView):
    """
    Create and List Employees view
    """
    queryset = EmployeesModel.objects.all()
    serializer_class = EmployeeSerializer


class EmployeesByDeptView(ListCreateAPIView):
    """
    Employees by department view
    """
    queryset = EmployeesModel.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = EmployeesModel.objects.all()
        dep_name = self.request.query_params.get('dept_name')
        if dep_name is not None:
            queryset = queryset.filter(dept_name=dep_name)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = queryset.count()
        return Response({"count": count})


class FindEmployeesView(ListAPIView):
    """
    Find employees with the given condition
    """
    queryset = EmployeesModel.objects.all()
    serializer_class = EmployeeSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['emp_name']

    def get_queryset(self):
        emp_name = self.request.query_params.get('emp_name')
        if emp_name is not None:
            queryset = EmployeesModel.objects.filter(emp_name__startswith=emp_name)
            return queryset
        return self.queryset


class EmployeesByIdView(APIView):
    """
    Retrieve employees by id
    """
    def get_object(self, pk):
        try:
            return EmployeesModel.objects.get(pk=pk)
        except EmployeesModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

