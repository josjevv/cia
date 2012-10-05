# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Project
import datetime

def dashboard(request):
    project_list = Project.objects.filter(start_date__lte=datetime.date.today())
    context = {
        'current_projects': project_list
    }

    print project_list

    return render(request, 'dashboard.html', context)