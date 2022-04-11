from django.test import TestCase
from ..models import Unidade

class TestCrudUnidade(TestCase):
    def test_create_unidade(self):
        fga = Unidade.objects.create(nome="Faculdade do Gama")
        fga_pesquisa = Unidade.objects.filter(nome="Faculdade do Gama")
        assert fga_pesquisa is not None
