from api.services import IndicaaServices
from django.test import TestCase
from api.models import Materia, Turma, Unidade
import pytest

class TestServices():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.indicaa = IndicaaServices()

    def test_criar_unidade(self, db):
        unidade = self.indicaa.criar_unidade("INSTITUTO DE ZOOLOGIA")
        assert unidade.nome == "INSTITUTO DE ZOOLOGIA"

    def test_criar_materia(self, db):
        unidade = self.indicaa.criar_unidade("INSTITUTO DE ZOOLOGIA")
        materia = self.indicaa.criar_materia("COMPILADORES", 'FGA0000', unidade)
        assert materia.nome == "COMPILADORES"
