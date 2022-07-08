from django.db import models

from turmas.models import Turma

class Agendamentos(models.Model):
    horario = models.DateTimeField()
    disciplina= models.CharField(max_length=100)
    descricao= models.CharField(max_length=500)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

def __str__(self):
    return self.disciplina