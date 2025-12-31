from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, role='default', **extra_fields):
        """Cria usuário personalizado no sistema"""
        if not username:
            raise ValueError("O nome de usuário não pode ser vazio!")
        
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        """Define os extra_fields para criar um um super user"""
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, role='admin', **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', "Administrador"),
        ('default', "Usuário Padrão")
    )

    username = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

# class Team(models.Model):
#     team_name = models.CharField(max_length=200)
#     leader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
#     members = models.ManyToManyField(CustomUser, related_name='teams', blank=True)

#     def __str__(self):
#         return self.team_name
