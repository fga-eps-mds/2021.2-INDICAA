from django.db import models

# Create your models here.


class Departamento(models.Model):
    name = models.CharField(max_length=255, primary_key=True) #, help_text='Ex.: Faculdade do Gama'

    def __str__(self):
        return self.name


class Materia(models.Model):
    name = models.CharField(max_length=255)
    codigoMateria = models.CharField(max_length=10, primary_key=True)
    cargaHoraria = models.CharField(max_length=3) 
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name





