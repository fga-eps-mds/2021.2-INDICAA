# As seguintes importacoes podem ser utilizadas futuramente 
from pydoc import classname
# Essas dependências importadas foram utilizadas no decorrer do código
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
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

# Esse método é responsável por percorrer todas as turmas, pegando a quantidade de vagas ocupadas em cada turma, 
# ao percorrer, guarda em uma lista de dicts e printa esta, esse tambem calcula e retorna a quantidade total de alunos matriculados
# em materias do departamento
def vagasOcupadasTurma():
    turmas = []
    contadorDocentes = 0
    contadorVagas = 0
    contadorTurmas = 0
    # Pega todos os elementos que possuem o mesmo xpath
    element1 = driver.find_elements(By.XPATH,
                                    "//td[@style='text-align: center;']")
    # Percorre cada elemento, procura o nome da turma e guarda em um dict
    for x in element1:
        resto = contadorTurmas % 2
        vagasOcupadas = x.get_attribute('innerHTML')
        anoSemestre = (driver.find_element(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr[2]/td[2]")).get_attribute('innerHTML')
        # Verifica se o item da lista é par ou ímpar, o numero de vagas ocupadas estao nos impares
        if resto == 1: 
            ano, semestre = anoSemestre.split(".")
            codigoTurma = (driver.find_elements(By.CLASS_NAME, "turma")[contadorDocentes]).get_attribute('innerHTML')
            local = (driver.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[contadorDocentes].find_elements(By.XPATH, "//td[8]")[contadorDocentes]).get_attribute('innerHTML').strip()
            horario = (driver.find_elements(By.XPATH, "//*[@id='turmasAbertas']/table/tbody/tr")[contadorDocentes].find_elements(By.XPATH, "//td[4]")[contadorDocentes]).get_attribute('innerText').strip()
            contadorVagas += int(vagasOcupadas)
            disciplina = driver.find_elements(By.XPATH,
                                    "//td[@class='nome']")[contadorDocentes]
        
            turma = disciplina.get_attribute('innerHTML')
            # As linhas seguintes separam o nome da turma da sua carga horaria
            docente, cargaHoraria = turma.split(" (")
            cargaHoraria, branco = cargaHoraria.split(")")
            # Coloca o dict da turma dentro de uma lista de turmas
            turmas.append({"docente": docente,
                          "codigoTurma": codigoTurma,
                          "horario": horario,
                          "vagasOcupadas": vagasOcupadas,
                          "cargaHoraria": cargaHoraria,
                          "local": local,
                          "ano": ano,
                          "semestre": semestre})

            contadorDocentes += 1
        contadorTurmas+=1
    pp.pprint(turmas)
    return contadorVagas
# O método abaixo é o responsável por percorrer as materias, as turmas relacionadas e somar todas as vagas ocupadas
# em cada materia do departamento
def alunosPorDisciplina():
    atual=0
    atualSoma=0
    atualDisc=0
    soma=0
    resultado = []
    # A linha de código a seguir pega todos os campos com tr e guarda em uma lista
    lista = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr')
    # Percorre cada elemento da lista
    for _ in lista:
        # Pega cada linha de tr, de acordo com a sua posição na lista e guarda em linha
        linha = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr')[atual]
        # Verifica se o classname da linha é 'linhaPar' ou 'linhaImpar', ou seja, se a linha corresponde a uma turma, se sim, pega a quantidade 
        # de vagas ocupadas e soma a variavel soma
        if linha.get_attribute("class") == 'linhaPar' or linha.get_attribute("class") == 'linhaImpar':
            linhaUsada = driver.find_elements(By.XPATH,
                                    '//*[@id="turmasAbertas"]/table/tbody/tr/td[7]')[atualSoma]
            conteudo = linhaUsada.get_attribute('innerHTML')
            soma=soma + int(conteudo)
            atualSoma+=1
        # Se a linha tiver classname agrupador, ou seja, for uma materia, armazena no dict o titulo da disciplina e o codigo
        # e ao final, zera a soma de vagas ocupadas
        if linha.get_attribute("class") == 'agrupador':
            linhaUsada = driver.find_elements(By.XPATH,
                                    "//span[@class='tituloDisciplina']")[atualDisc]
            conteudo = linhaUsada.get_attribute('innerHTML')
            # Separa o titulo da materia do codigo 
            codigoMateria, nome = conteudo.split(" - ")
            resultado.append({"nome":nome,
                              "codigoMateria": codigoMateria})

            if atualDisc==0:
                atualDisc+=1
            else:
                resultado[atualDisc-1]["matriculados"] = soma
                atualDisc+=1
                
            soma=0
        atual+=1
    # Acrescenta as informacoes de vagas ocupadas do ultimo elemento da lista no dict
    resultado[atualDisc-1]["matriculados"] = soma
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
    vagasOcupadasTotal = vagasOcupadasTurma()
    print(f'Numero de Alunos encontrados: {vagasOcupadasTotal}')
    materias = alunosPorDisciplina()
    resultado = {'nome': 'Faculdade do Gama',
                 'vagasOcupadasTotal': vagasOcupadasTotal,
                 'materias': materias}
    pp.pprint(resultado)
    fecharJanela()


main()
