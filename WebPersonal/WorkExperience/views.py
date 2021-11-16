from django.shortcuts import render
from .models import Project

# Create your views here.
def work(request):
    projects = Project.objects.all()
    return render(request, "workexperiense/work.html", {'projects':projects})