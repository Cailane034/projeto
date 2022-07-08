from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from turmas.models import Turma


class UserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get('is_staff') is not True:
        raise ValueError(_('Superuser must have is_staff=True.'))
    if extra_fields.get('is_superuser') is not True:
        raise ValueError(_('Superuser must have is_superuser=True.'))
    return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
  cargos = [
    ('PF', 'Professor'),
    ('AL', 'Aluno')
  ]
  username = None
  matricula = models.CharField('Matrícula', max_length=20, unique=True)
  cargo = models.CharField(max_length=2, choices=cargos, default='AL')

  objects = UserManager()

  USERNAME_FIELD = 'matricula'


class User_Turma(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  turma = models.ForeignKey(Turma, on_delete=models.CASCADE)



