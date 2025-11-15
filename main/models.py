from django.db import models
import os
from uuid import uuid4

def project_image_path(instance, filename):
    """Generate unique path for project images"""
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join('projects', filename)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    career_objective = models.TextField()
    
    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=300)
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    achievements = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured_image = models.ImageField(upload_to=project_image_path, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def image_url(self):
        if self.featured_image and hasattr(self.featured_image, 'url'):
            return self.featured_image.url
        return '/static/images/project-placeholder.jpg'

class Certification(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=10, blank=True)
    
    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title