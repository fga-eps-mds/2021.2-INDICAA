from cgitb import lookup
from django.forms import UUIDField
from .models import Materia, Unidade, Turma
from rest_framework import serializers


class UnidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidade
        fields = ['nome']


class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('nome', 'codigoMateria', 'cargaHoraria', 'unidade')

        
class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turma
        fields = ('idTurma', 'docente', 'codigoTurma', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'ano', 'semestre', 'materia')
        