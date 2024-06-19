from django.shortcuts import render
from .models import Project, Skill, Experience

def portfolio_homepage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
        'experience': experience,
    }
    return render(request, 'portfolio/index.html', context)
