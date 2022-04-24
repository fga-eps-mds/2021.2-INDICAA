from django.test import TestCase
from ..models import Unidade

class TestCrudUnidade(TestCase):
    def test_create_unidade(self):
        fga = Unidade.objects.create(nome="Faculdade do Gama")
        fga_pesquisa = Unidade.objects.filter(nome="Faculdade do Gama").last()
        assert fga_pesquisa is not None
        assert fga_pesquisa.nome == 'Faculdade do Gama'

    def update_unidade(self):
        Unidade.objects.create(nome="Faculdade do Gama")
        fga = Unidade.objects.filter(nome="Faculdade do Gama")
        Unidade.objects.update(nome='Faculdade de direito')
        assert fga.nome == 'Faculdade de direito'

    def delete_unidade(self):
        Unidade.objects.create(nome="Faculdade do Gama")
        fga = Unidade.objects.filter(nome="Faculdade do Gama")
        Unidade.objects.delete()
        assert fga is None
