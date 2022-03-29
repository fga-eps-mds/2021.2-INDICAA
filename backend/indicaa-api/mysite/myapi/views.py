from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import MateriaSerializer, DepartamentoSerializer
from .models import Materia, Departamento

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all().order_by('name')
    serializer_class = MateriaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by('name')
    serializer_class = DepartamentoSerializer
