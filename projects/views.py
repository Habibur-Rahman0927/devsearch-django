from django.shortcuts import render
from .models import Project
from .forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project.html', context)


def singleProject(request, pk):
    projectObj = Project.objects.get(id = pk)
    
    return render(request, 'projects/single-porject.html', {'projectObj': projectObj})

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)