from django.db import models

class employee(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_id = models.IntegerField(unique=True, auto_created=True)
    Employee_email = models.EmailField(unique=True)
    Employee_salary = models.FloatField()