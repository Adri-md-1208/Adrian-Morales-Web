from django.shortcuts import render
from projects.models import Project

def projects(request):

    """
    Projects I am working on
    """
    projects = Project.objects.all()

    return render(request, "projects/projects.html", {'projects': projects})

