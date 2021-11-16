from django.shortcuts import render
from .models import Project

# Create your views here.
def skills(request):
    projects = Project.objects.all()
    return render(request, "skills/skills.html", {'projects':projects})
