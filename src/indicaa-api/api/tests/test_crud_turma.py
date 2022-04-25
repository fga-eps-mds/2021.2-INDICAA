from django.test import TestCase
from ..models import Materia, Unidade, Turma
import pytest

class TestCrudturma(TestCase):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.unidade = Unidade.objects.create(nome="FACULDADE DE BIOLOGIA")
        self.materia = Materia.objects.create(codigoMateria='FGA0000', nome='COMPILADORES', cargaHoraria='60h', unidade=self.unidade)

    def test_create_turma(self):
        id = Turma.objects.create(
            docente="FERNANDA ALVES",
            codigoTurma='A',
            horario='46T23',
            vagasOfertadas='60',
            vagasOcupadas='40',
            local='remoto',
            ano='2021',
            semestre='2',
            materia=self.materia
        ).idTurma
        turma = Turma.objects.filter(idTurma=id).last()
        assert turma is not None
        assert turma.docente == "FERNANDA ALVES"

    def update_turma(self):
        id = Turma.objects.create(
            docente="FERNANDA ALVES",
            codigoTurma='A',
            horario='46T23',
            vagasOfertadas='60',
            vagasOcupadas='40',
            local='remoto',
            ano='2021',
            semestre='2',
            materia=self.materia
        ).idTurma
        turma = Turma.objects.filter(idTurma=id).last()
        Turma.objects.update(docente='JOAO FERREIRA', horario='23M12')
        assert turma.nome == 'JOAO FERREIRA'

    def delete_turma(self):
        id = Turma.objects.create(
            docente="FERNANDA ALVES",
            codigoTurma='A',
            horario='46T23',
            vagasOfertadas='60',
            vagasOcupadas='40',
            local='remoto',
            ano='2021',
            semestre='2',
            materia=self.materia
        ).idTurma
        turma = Turma.objects.filter(idTurma=id).last()
        Turma.objects.delete()
        assert turma is None