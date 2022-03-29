from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CursoSerializer, DepartamentoSerializer
from .models import Curso, Departamento

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('name')
    serializer_class = CursoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by('name')
    serializer_class = DepartamentoSerializer
