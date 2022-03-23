from .models import Curso
from rest_framework import serializers

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = ('name', 'campus')
