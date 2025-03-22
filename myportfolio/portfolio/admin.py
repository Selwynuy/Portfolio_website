from django.contrib import admin
from .models import Project, SkillCategory, Skill, TimelineEvent, Achievement

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'github_url']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]