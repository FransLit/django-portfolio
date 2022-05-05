from django.shortcuts import render
from .models import Project, Skill, About

def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'foliapp/home.html', {'projects':projects, 'skills': skills})

def about(request):
    texts = About.objects.all()
    return render(request, 'foliapp/about.html', {'texts': texts})

