from .models import Unidade, Turma, Materia

class IndicaaServices:
    def criar_unidade(self, nomeUnidade):
        unidade = Unidade.objects.filter(nome=nomeUnidade).last()
        if(unidade==None):
            unidade = Unidade.objects.create(
                nome=nomeUnidade
            )
        return unidade
    
    def criar_materia(self, nome, codigoMateria, unidade):
        materia_teste = Materia.objects.filter(codigoMateria=codigoMateria).last()
        if(materia_teste==None):
            materia_teste = Materia.objects.create(
                nome=nome,
                codigoMateria=codigoMateria,
                cargaHoraria="",
                unidade=unidade
            )
            materia_teste.save()
        return materia_teste

    def atualizar_materia(self, codigoMateria, cargaHoraria):
        Materia.objects.filter(codigoMateria=codigoMateria).update(cargaHoraria=cargaHoraria)

    def criar_turma(self, professor, codigoTurma, vagasOcupadas, vagasOfertadas, local, horario, semestre, ano, materia):
        turma_teste = Turma.objects.filter(materia=materia, docente=professor, codigoTurma=codigoTurma).last()
        if(turma_teste==None):
            turma_teste = Turma.objects.create(
                docente=professor,
                codigoTurma=codigoTurma,
                vagasOcupadas=vagasOcupadas,
                vagasOfertadas=vagasOfertadas,
                local=local,
                horario=horario,
                semestre=semestre,
                ano=ano,
                materia=materia
            )
            turma_teste.save()