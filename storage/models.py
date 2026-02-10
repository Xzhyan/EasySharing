from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Para checar nomes de arquivos e evitar duplicatas
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            self.delete(name)
        return name


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    leader_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='teams', blank=True)

    def __str__(self):
        return self.team_name


class Folder(models.Model):
    folder_name = models.CharField(max_length=100, null=False)
    folder_path = models.CharField(max_length=100, null=False)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.folder_name


class Archive(models.Model):
    archive = models.FileField(upload_to='main/', storage=OverwriteStorage())
    file_name = models.CharField(max_length=200, unique=True)
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE, null=False)
    size = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name
