# As seguintes importacoes podem ser utilizadas futuramente 
from pydoc import classname
# Essas dependências importadas foram utilizadas no decorrer do código
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from api.models import Unidade, Materia, Turma
import pprint as pp
materias = []

# Configuração do navegador (Firefox)
option = Options()
option.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=option)

# A seguinte funcao acessa a URL do SIGAA, em que será realizado o web scaping
def acessarURL():
    url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"
    driver.get(url)

# Seleciona o nível de ensino na consulta, no caso, graduacao
def selecionarNivelEnsino():
    botaoCampoEnsino = driver.find_element(By.ID, 'formTurma:inputNivel')
    botaoGraduacao = driver.find_element(By.XPATH, '//*[@id="formTurma:inputNivel"]/option[3]')
    botaoCampoEnsino.click()
    botaoGraduacao.click()

# Seleciona o semestre que deseja consultar
def selecionarSemestre():    
    inputAno = driver.find_element(By.ID, "formTurma:inputAno")
    inputAno.click()
    inputAno.send_keys(Keys.CONTROL, 'a')
    inputAno.send_keys('2021')
    botaoSemestre=driver.find_element(By.XPATH, '//*[@id="formTurma:inputPeriodo"]/option[2]')
    botaoSemestre.click()

# Seleciona a unidade da UnB para a busca, nesse caso, a Faculdade do Gama
def selecionarUnidade():
    botaoUnidade = driver.find_element(By.ID, 'formTurma:inputDepto')
    botaoFGA = driver.find_element(By.XPATH, '//*[@id="formTurma:inputDepto"]/option[79]')
    botaoUnidade.click()
    botaoFGA.click()

# Clica no botao buscar para visualizar o resultado da consulta
def acionarBotaoBuscar():
    botaoBuscar = driver.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11')
    botaoBuscar.click()

def percorreTurmas(atualSoma, soma, materia, codigoMateria):
    linhaUsada = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')[atualSoma]
    conteudo = linhaUsada.get_attribute('innerHTML')
    soma=soma + int(conteudo)
    anoSemestre = (driver.find_element(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr[2]/td[2]")).get_attribute('innerHTML')
    ano, semestre = anoSemestre.split(".")
    codigoTurma = (driver.find_elements(By.CLASS_NAME, "turma")[atualSoma]).get_attribute('innerHTML')
    local = (driver.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[atualSoma].find_elements(By.XPATH, "//td[8]")[atualSoma]).get_attribute('innerHTML').strip()
    horario = (driver.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[atualSoma].find_elements(By.XPATH, "//td[4]")[atualSoma]).get_attribute('innerText').strip() 
    disciplina = driver.find_elements(By.XPATH,
                            "//td[@class='nome']")[atualSoma]
    turma = disciplina.get_attribute('innerHTML')
    professor, cargahoraria = turma.split(" (")
    cargahoraria, _ = cargahoraria.split(")") 

    turma_teste = Turma.objects.filter(materia=materia, docente=professor, codigoTurma=codigoTurma).last()
    if(turma_teste==None):
        turma_teste = Turma.objects.create(
            docente=professor,
            codigoTurma=codigoTurma,
            vagasOcupadas=conteudo,
            vagasOfertadas=0,
            local=local,
            horario=horario,
            semestre=semestre,
            ano=ano,
            materia=materia
        )
        turma_teste.save()
    Materia.objects.filter(codigoMateria=codigoMateria).update(cargaHoraria=cargahoraria)

def alunosPorDisciplina():
    unidade = Unidade.objects.filter(nome="Faculdade do Gama").last()
    if(unidade==None):
        unidade = Unidade.objects.create(
            nome="Faculdade do Gama"
        )
    atual=0
    atualSoma=0
    atualDisc=0
    soma=0
    resultado = []
    materia_teste = None
    codigoMateria=""

    lista = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr')

    for _ in lista:
    
        linha = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr')[atual]
        if linha.get_attribute("class") == 'agrupador':
            linhaUsada = driver.find_elements(By.XPATH,
                                    "//span[@class='tituloDisciplina']")[atualDisc]
            conteudo = linhaUsada.get_attribute('innerHTML')

            codigoMateria, nome = conteudo.split(" - ")
            resultado.append({"nome":nome,
                              "codigoMateria": codigoMateria})

            # if atualDisc==0:
            #     atualDisc+=1
            # else:
                # resultado[atualDisc-1]["matriculados"] = soma
            atualDisc+=1
                
            soma=0
            materia_teste = Materia.objects.filter(codigoMateria=codigoMateria).last()
            if(materia_teste==None):
                materia_teste = Materia.objects.create(
                    nome=nome,
                    codigoMateria=codigoMateria,
                    cargaHoraria="qualquer",
                    unidade=unidade
                )
                materia_teste.save()

        if linha.get_attribute("class") == 'linhaPar' or linha.get_attribute("class") == 'linhaImpar':
            percorreTurmas(atualSoma, soma, materia_teste, codigoMateria)
            # linhaUsada = driver.find_elements(By.XPATH,
            #                         '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')[atualSoma]
            # conteudo = linhaUsada.get_attribute('innerHTML')
            # soma=soma + int(conteudo)
            atualSoma+=1

        
        atual+=1
    # resultado[atualDisc-1]["matriculados"] = soma
    return resultado
    
    

# Fecha o navegador
def fecharJanela():
    driver.quit()

def main():
    acessarURL()
    driver.implicitly_wait(6)
    selecionarNivelEnsino()
    selecionarUnidade()
    selecionarSemestre()
    acionarBotaoBuscar()
    # vagasOcupadasTotal = vagasOcupadasTurma()
    # print(f'Numero de Alunos encontrados: {vagasOcupadasTotal}')
    materias = alunosPorDisciplina()
    resultado = {'nome': 'Faculdade do Gama',
                #  'vagasOcupadasTotal': vagasOcupadasTotal,
                 'materias': materias}
    pp.pprint(resultado)
    fecharJanela()


main()
