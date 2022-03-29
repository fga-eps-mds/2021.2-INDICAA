from django.db import models

# Create your models here.

class Curso(models.Model):
    name = models.CharField(max_length = 50)
    campus = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Departamento(models.Model):
    name = models.CharField(max_length=100, primary_key=True) #, help_text='Ex.: Faculdade do Gama'

    def __str__(self):
        return self.name


