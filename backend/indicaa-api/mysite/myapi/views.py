from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import MateriaSerializer, DepartamentoSerializer, TurmaSerializer
from .models import Materia, Departamento, Turma


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by('nome')
    serializer_class = DepartamentoSerializer


class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all().order_by('departamento')
    serializer_class = MateriaSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all().order_by('materia')
    serializer_class = TurmaSerializer
