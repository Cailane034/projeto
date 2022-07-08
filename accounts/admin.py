from django.contrib import admin

from .models import CustomUser, User_Turma

admin.site.register([CustomUser, User_Turma])