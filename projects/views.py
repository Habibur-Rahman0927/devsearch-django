from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects/project.html')


def singleProject(request, pk):
    return render(request, 'projects/single-porject.html')