from django.db import models

# Project model
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    def __str__(self):
        return self.title



# Skill model
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"
    

# Timeline model
class TimelineEvent(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
# Achievements model
class Achievement(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
