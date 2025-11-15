from django.shortcuts import render, get_object_or_404
from .models import Profile, Education, SkillCategory, Experience, Project, Certification, Achievement

def home(request):
    """Home page view with all portfolio data"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
        
    education = Education.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skill_set').all()
    experiences = Experience.objects.all()
    projects = Project.objects.filter(is_featured=True)
    certifications = Certification.objects.all()
    achievements = Achievement.objects.all()
    
    context = {
        'profile': profile,
        'education': education,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'projects': projects,
        'certifications': certifications,
        'achievements': achievements,
    }
    return render(request, 'main/home.html', context)

def projects_list(request):
    """All projects list view"""
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
    }
    return render(request, 'main/projects_list.html', context)

def project_detail(request, project_id):
    """Individual project detail view"""
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project,
    }
    return render(request, 'main/project_detail.html', context)