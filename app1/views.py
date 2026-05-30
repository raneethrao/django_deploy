from django.shortcuts import render

# Create your views here.

from app1.models import employee
from app1.form import Employee_form

def emp_details(request):
    data = employee.objects.all()
    form = Employee_form()
    context = {
        'data':data,
        'form':form
    }
    return render(request,'app1_Temp/home.html',context)


