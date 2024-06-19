from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies_used = models.TextField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    link = models.URLField(max_length=255, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField()
