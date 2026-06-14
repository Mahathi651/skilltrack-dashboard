from django.shortcuts import render
from .models import Skill, Project


def home(request):
    return render(request, 'dashboard/home.html')


def skills(request):
    skills_data = Skill.objects.all()
    return render(request, 'dashboard/skills.html', {'skills': skills_data})


def projects(request):
    projects_data = Project.objects.all()
    return render(request, 'dashboard/projects.html', {'projects': projects_data})


def internships(request):
    return render(request, 'dashboard/internships.html')


def analytics(request):
    skills_data = Skill.objects.all()
    projects_data = Project.objects.all()

    total_skills = skills_data.count()
    total_projects = projects_data.count()

    if total_skills > 0:
        total_progress = sum(skill.progress for skill in skills_data)
        average_progress = total_progress // total_skills
    else:
        average_progress = 0

    return render(request, 'dashboard/analytics.html', {
        'total_skills': total_skills,
        'total_projects': total_projects,
        'average_progress': average_progress,
    })


def settings_page(request):
    return render(request, 'dashboard/settings.html')


def contact(request):
    return render(request, 'dashboard/contact.html')