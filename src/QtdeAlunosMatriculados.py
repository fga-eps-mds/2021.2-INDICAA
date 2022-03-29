# As seguintes importacoes podem ser utilizadas futuramente 
from pydoc import classname
import time
import requests
# Essas dependências importadas foram utilizadas no decorrer do código
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
materias = []

# Configuração do navegador (Firefox)
option = Options()
option.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

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


def vagasOcupadasTurma():
    turmas = []
    contadorDocentes = 0
    contadorVagas = 0
    contadorTurmas = 0
    element1 = driver.find_elements(By.XPATH,
                                    "//td[@style='text-align: center;']")
   
    for x in element1:
        resto = contadorTurmas % 2
        numeroAlunos = x.get_attribute('innerHTML')
        if resto == 1: 
            contadorVagas += int(numeroAlunos)
            disciplina = driver.find_elements(By.XPATH,
                                    "//td[@class='nome']")[contadorDocentes]
        
            turma = disciplina.get_attribute('innerHTML')
            professor, cargahoraria = turma.split(" (")
            cargahoraria, branco = cargahoraria.split(")")
            turmas.append({"turma": professor,
                          "matriculados": numeroAlunos,
                          "carga-horaria": cargahoraria})

            print(turmas)
            contadorDocentes += 1
        contadorTurmas+=1
    return contadorVagas

def alunosPorDisciplina():
    atual=0
    Disc=[]
    Soma=[]
    atualSoma=0
    atualDisc=0
    soma=0
    resultado = []
    lista = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr')
    for x in lista:
        linha = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr')[atual]
        if linha.get_attribute("class") == 'linhaPar' or linha.get_attribute("class") == 'linhaImpar':
            linhaUsada = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')[atualSoma]
            conteudo = linhaUsada.get_attribute('innerHTML')
            soma=soma + int(conteudo)
            atualSoma+=1
        if linha.get_attribute("class") == 'agrupador':
            linhaUsada = driver.find_elements(By.XPATH,
                                    "//span[@class='tituloDisciplina']")[atualDisc]
            conteudo = linhaUsada.get_attribute('innerHTML')
            Disc.append(conteudo)
            if atualDisc==0:
                atualDisc+=1
            else:
                Soma.append(soma)
                atualDisc+=1
            soma=0
            
        atual+=1

    Soma.append(soma)

    for x in Disc:
        codigo, materia = x.split(" - ")
        resultado.append({"disciplina":materia,
                          "codigo": codigo})
    num=0
    for y in Soma:
        resultado[num]["matriculados"] = y
        num+=1

    return resultado
    
    

# Fecha o navegador
def fecharJanela():
    driver.quit()

# Função principal, chama todas as outras funções anteriores
def main():
    acessarURL()
    driver.implicitly_wait(6)
    selecionarNivelEnsino()
    selecionarUnidade()
    selecionarSemestre()
    acionarBotaoBuscar()
    contadorVagas = vagasOcupadasTurma()
    print(f'Numero de Alunos encontrados: {contadorVagas}')
    alunos = alunosPorDisciplina()
    #print(alunosPorDisciplina())
    resultado = {'departamento': 'Faculdade do Gama',
                 'numAlunos': contadorVagas,
                 'materias': alunos}
    print(resultado)
    fecharJanela()


main()
