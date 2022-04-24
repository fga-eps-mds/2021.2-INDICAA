# from types import NoneType
from django.db import models

# Create your models here.


class Unidade(models.Model):
    nome = models.CharField(
        max_length=255, 
        primary_key=True
    )



class Materia(models.Model):
    codigoMateria = models.CharField(
        max_length=70, 
        primary_key=True
    )
    nome = models.CharField(
        max_length=255
    )
    cargaHoraria = models.CharField(
        max_length=50
    ) 
    unidade = models.ForeignKey(
        Unidade, 
        on_delete=models.RESTRICT
    )

    def __str__(self):
        return self.nome


class Turma(models.Model):
    idTurma = models.AutoField(
        primary_key=True
    )
    docente = models.CharField(
        max_length=255
    )
    codigoTurma = models.CharField(
        max_length=50
    )
    horario = models.CharField(
        max_length=170
    )
    vagasOfertadas = models.IntegerField()
    vagasOcupadas = models.IntegerField()
    local = models.CharField(
        max_length=255
    )
    semestre = models.IntegerField()
    ano = models.IntegerField()
    materia = models.ForeignKey(
        Materia, 
        on_delete=models.RESTRICT
    )

    def __str__(self):
        return self.docente





