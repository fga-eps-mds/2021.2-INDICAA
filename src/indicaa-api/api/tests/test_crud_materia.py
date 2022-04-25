from django.test import TestCase
from ..models import Materia, Unidade

class TestCrudMateria(TestCase):
    def test_create_materia(self):
        unidade = Unidade.objects.create(nome="FACULDADE DE BIOLOGIA")
        materia = Materia.objects.create(codigoMateria='FGA0000', nome='COMPILADORES', cargaHoraria='60h', unidade=unidade)
        materia = Materia.objects.filter(codigoMateria='FGA0000').last()
        assert materia is not None
        assert materia.codigoMateria == 'FGA0000'

    def update_materia(self):
        unidade = Unidade.objects.create(nome="FACULDADE DE BIOLOGIA")
        Materia.objects.create(codigoMateria='FGA0000', nome='COMPILADORES', cargaHoraria='60h', unidade=unidade)
        nomeMateria = Materia.objects.filter(nome='COMPILADORES')
        Materia.objects.update(nome='DEEP LEARNING')
        assert nomeMateria.nome == 'DEEP LEARNING'

    def delete_materia(self):
        unidade = Unidade.objects.create(nome="FACULDADE DE BIOLOGIA")
        Materia.objects.create(codigoMateria='FGA0000', nome='COMPILADORES', cargaHoraria='60h', unidade=unidade)
        materia_teste = Materia.objects.filter(nome='COMPILADORES')
        Materia.objects.delete()
        assert materia_teste  is None