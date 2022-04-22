from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .services import IndicaaServices
from rest_framework import viewsets
from .serializers import MateriaSerializer, UnidadeSerializer, TurmaSerializer
from .models import Materia, Unidade, Turma
from django.http import HttpResponse
import sys


class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all().order_by('nome')
    serializer_class = UnidadeSerializer
    if "runserver" in sys.argv:
            from scraping.QtdeAlunosMatriculados import main
            main()
        

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all().order_by('codigoMateria')
    serializer_class = MateriaSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all().order_by('materia')
    serializer_class = TurmaSerializer
