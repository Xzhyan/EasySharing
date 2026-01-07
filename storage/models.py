from django.db import models
from django.conf import settings

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    leader_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams', blank=True)

    def __str__(self):
        return self.team_name

class Folder(models.Model):
    folder_name = models.CharField(max_length=100)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folder_name

class Archive(models.Model):
    archive = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=200)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    size = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name
