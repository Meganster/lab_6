from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Department

# Create your views here..


def index(request):
    department = Department.objects.all()
    content = {
        'departments': department
    }
    for a in department:
        print(a)
    return render(request, 'departments.html', content)


def department(request, id):
    department = Department.objects.get(id=int(id))
    content = {
        'department' : department
    }
    return render(request, 'single.html', content)
    pass
