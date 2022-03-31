from .models import Materia, Departamento, Turma
from rest_framework import serializers


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ['nome']


class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('nome', 'codigoMateria', 'cargaHoraria', 'departamento')

        
class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turma
        fields = ('idTurma', 'docente', 'codigoTurma', 'horario', 'vagasOfertadas', 'vagasOcupadas', 'local', 'ano', 'semestre', 'materia')
