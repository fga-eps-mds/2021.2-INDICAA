# As seguintes importacoes podem ser utilizadas futuramente 
from pydoc import classname
# Essas dependências importadas foram utilizadas no decorrer do código
from api.services import IndicaaServices
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import pprint as pp

# unidade = None
indicaa = IndicaaServices()
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
    botaoSemestre = driver.find_element(By.XPATH, '//*[@id="formTurma:inputPeriodo"]/option[2]')
    botaoSemestre.click()


# Seleciona a unidade da UnB para a busca, nesse caso, a Faculdade do Gama
def selecionarUnidade(n):
    botaoUnidade = driver.find_element(By.ID, 'formTurma:inputDepto')
    botaoFGA = driver.find_elements(By.XPATH, '//*[@id="formTurma:inputDepto"]/option')
    botaoFGA = botaoFGA[n]
    nomeUnidade = botaoFGA.get_attribute('innerHTML')
    # indicaa = IndicaaServices()
    # unidade =  indicaa.criar_unidade(nomeUnidade)
    botaoUnidade.click()
    botaoFGA.click()
    return nomeUnidade


# Clica no botao buscar para visualizar o resultado da consulta
def acionarBotaoBuscar():
    botaoBuscar = driver.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11')
    botaoBuscar.click()


def percorreTurmas(atualSoma, soma, materia, codigoMateria):
    vagasOcupadas = driver.find_elements(By.XPATH,
                                         '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')[atualSoma].get_attribute(
        'innerHTML')
    vagasOfertadas = driver.find_elements(By.XPATH,
                                          '//*[@id="turmasAbertas"]/table/tbody/tr/td[6]')[atualSoma].get_attribute(
        'innerHTML')
    soma = soma + int(vagasOcupadas)
    anoSemestre = (driver.find_element(By.XPATH,
                                       "//*[@id='turmasAbertas']/table/tbody/tr[2]/td[2]")).get_attribute('innerHTML')
    ano, semestre = anoSemestre.split(".")
    codigoTurma = (driver.find_elements(By.CLASS_NAME, "turma")[atualSoma]).get_attribute('innerHTML')
    local = (
    driver.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[atualSoma].find_elements(By.XPATH,
                                                                                                       "//td[8]")[
        atualSoma]).get_attribute('innerHTML').strip()
    horario = (
    driver.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[atualSoma].find_elements(By.XPATH,
                                                                                                       "//td[4]")[
        atualSoma]).get_attribute('innerText').strip()
    disciplina = driver.find_elements(By.XPATH,
                                      "//td[@class='nome']")[atualSoma]
    turma = disciplina.get_attribute('innerHTML')
    professor, cargahoraria = turma.split(" (")
    cargahoraria, _ = cargahoraria.split(")")

    indicaa = IndicaaServices()
    indicaa.criar_turma(professor, codigoTurma, vagasOcupadas, vagasOfertadas, local, horario, semestre, ano, materia)
    indicaa.atualizar_materia(codigoMateria, cargahoraria)


def alunosPorDisciplina():
    atual = 0
    atualSoma = 0
    atualDisc = 0
    soma = 0
    resultado = []
    materia_teste = None
    codigoMateria = ""

    lista = driver.find_elements(By.XPATH,
                                 '//*[@id="turmasAbertas"]/table/tbody/tr')

    for _ in lista:

        linha = driver.find_elements(By.XPATH,
                                     '//*[@id="turmasAbertas"]/table/tbody/tr')[atual]
        if linha.get_attribute("class") == 'agrupador':
            linhaUsada = driver.find_elements(By.XPATH,
                                              "//span[@class='tituloDisciplina']")[atualDisc]
            conteudo = linhaUsada.get_attribute('innerHTML')

            conteudo = conteudo.split(" - ")
            codigoMateria = conteudo[0]
            nome = conteudo[1]
            if len(conteudo) == 3:
                nome = nome + " - " + conteudo[2]
            resultado.append({"nome": nome,
                              "codigoMateria": codigoMateria})

            # if atualDisc==0:
            #     atualDisc+=1
            # else:
            # resultado[atualDisc-1]["matriculados"] = soma
            atualDisc += 1

            unidade = indicaa.criar_unidade(selecionarUnidade(52))

            soma = 0
            # indicaa = IndicaaServices()
            materia_teste = indicaa.criar_materia(nome, codigoMateria, unidade)

        if linha.get_attribute("class") == 'linhaPar' or linha.get_attribute("class") == 'linhaImpar':
            percorreTurmas(atualSoma, soma, materia_teste, codigoMateria)
            atualSoma += 1

        atual += 1
    # resultado[atualDisc-1]["matriculados"] = soma
    return resultado


# Fecha o navegador
def fecharJanela():
    driver.quit()


def main():
    acessarURL()
    driver.implicitly_wait(6)
    selecionarNivelEnsino()
    # for i in range(2, 10):
    nomeUnidade = selecionarUnidade(52)
    selecionarSemestre()
    acionarBotaoBuscar()
    alunos = alunosPorDisciplina()
    # print(alunos)
    # selecionarUnidade()
    # selecionarSemestre()
    # acionarBotaoBuscar()
    # vagasOcupadasTotal = vagasOcupadasTurma()
    # print(f'Numero de Alunos encontrados: {vagasOcupadasTotal}')
    materias = alunosPorDisciplina()
    resultado = {'nome': nomeUnidade,
                 #  'vagasOcupadasTotal': vagasOcupadasTotal,
                 'materias': materias}
    pp.pprint(resultado)
    fecharJanela()


main()

