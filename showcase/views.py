from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()  # Get all projects from the database
    return render(request, 'showcase/project_list.html', {'projects': projects})
