from django.contrib import admin
from .models import Profile, Education, SkillCategory, Skill, Experience, Project, Certification, Achievement

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_editable = ['email', 'phone']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'duration']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'created_at']
    list_filter = ['is_featured']
    list_editable = ['is_featured']
    search_fields = ['title', 'technologies']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'year']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title']