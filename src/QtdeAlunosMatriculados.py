# As seguintes importacoes podem ser utilizadas futuramente 
import time
import requests
# Essas dependências importadas foram utilizadas no decorrer do código
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys


# Configuração do navegador Firefox
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

# Faz a contagem da quantidade de alunos matriculados em cada turma e printa o resultado
# O formato de saída é: ""
def verificaVagasOcupadas():
    contadorDocentes = 0
    contadorVagas = 0
    contadorTurmas = 0
    element1 = driver.find_elements(By.XPATH,
                                    "//td[@style='text-align: center;']")
    element2 = driver.find_elements(By.CLASS_NAME, 'agrupador')
    for x in element1:
        resto = contadorTurmas % 2
        numeroAlunos = x.get_attribute('innerHTML')
        if resto == 1: 
            contadorVagas += int(numeroAlunos)
            disciplina = driver.find_elements(By.XPATH,
                                    "//td[@class='nome']")[contadorDocentes]
            turma = disciplina.get_attribute('innerHTML')
            print(f'Alunos Matriculados em {turma}: {numeroAlunos}')
            contadorDocentes += 1
        contadorTurmas+=1
    return contadorVagas

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
    contadorVagas = verificaVagasOcupadas()
    print(f'Numero de Turmas encontradas: {contadorVagas}')
    fecharJanela()


main()
