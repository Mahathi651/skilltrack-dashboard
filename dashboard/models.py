from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    progress = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)

    def __str__(self):
        return self.title