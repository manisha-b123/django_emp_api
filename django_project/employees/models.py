from django.db import models


# Create your models here.
class EmployeesModel(models.Model):
    """
    Employees model
    """
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=200)
    dept_name = models.CharField(max_length=200)


