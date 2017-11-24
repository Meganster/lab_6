from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Department
from .models import Employee

# Create your views here..


def index(request):
    department = Department.objects.all()
    content = {
        'departments': department
    }
    return render(request, 'departments.html', content)


def department(request, id):
    department = Department.objects.get(id=int(id))
    employers = Employee.objects.filter(department_id=int(id))
    
    content = {
        'department' : department,
        'employers': employers
    }
    return render(request, 'single.html', content)
