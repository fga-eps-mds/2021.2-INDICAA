from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CursoSerializer
from .models import Curso

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('name')
    serializer_class = CursoSerializer
