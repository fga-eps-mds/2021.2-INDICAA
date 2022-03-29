from .models import Materia, Departamento
from rest_framework import serializers

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('name', 'codigoMateria', 'cargaHoraria', 'departamento')


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ['name']