from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

# Configuração do Navegador (Firefox)
option = Options()
option.headless = True
servicoFirefox = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servicoFirefox, options=option)
# Acessar a página inicial da Consulta de Turmas do SIGAA
def acessarURL():
    url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"
    driver.get(url)

# Selecionando a opção da "Graduação"
def selecionarNivelEnsino():
    botaoCampoEnsino = driver.find_element(By.ID, 'formTurma:inputNivel')
    botaoGraduacao = driver.find_element(By.XPATH,
                                         '//*[@id="formTurma:inputNivel"]/option[3]')
    botaoCampoEnsino.click()
    botaoGraduacao.click()

# Função que pode ser usada para selecionar um semestre específico
# def selecionarSemestre():
#     inputAno = driver.find_element(By.ID, "formTurma:inputAno")
#     inputAno.click()
#     inputAno.send_keys(Keys.CONTROL, 'a')
#     inputAno.send_keys('2021')
#     botaoSemestre = driver.find_element(By.XPATH,
#         '//*[@id="formTurma:inputPeriodo"]/option[2]')
#     botaoSemestre.click()

# Selecionando a unidade especificada (FGA)
def selecionarUnidade():
    botaoUnidade = driver.find_element(By.ID, 'formTurma:inputDepto')
    botaoFGA = driver.find_element(By.XPATH,
                                   '//*[@id="formTurma:inputDepto"]/option[79]')
    botaoUnidade.click()
    botaoFGA.click()

# Buscando a listagem na unidade selecionada e no semestre especificado
def acionarBotaoBuscar():
    botaoBuscar = driver.find_element(By.NAME,
                                      'formTurma:j_id_jsp_1370969402_11')
    botaoBuscar.click()

# Realiza a contagem da quantidade de vagas disponíveis
# e as imprime conforme a turma em questão.
# Formato da saída: "Vagas Disponíveis em *nome do docente (qtd. horas)*: *nº de vagas disponíveis*"
def verificaVagas():
    contadorDocentes = 0
    contadorVagas = 0
    vagasTotais = 0
    element1 = driver.find_elements(By.XPATH,
                                    "//td[@style='text-align: center;']")  # lista com todas as quantidades de vagas disponíveis
    for x in element1:
        resto = contadorVagas % 2
        vagas = x.get_attribute('innerHTML')
        if resto == 0:
            vagasOfertadas = int(vagas, base=10)
        else:
            disciplina = driver.find_elements(By.XPATH,
                                              "//td[@class='nome']")[contadorDocentes]
            turma = disciplina.get_attribute('innerHTML')
            numeroAlunos = int(vagas, base=10)
            vagasDisponiveis = vagasOfertadas - numeroAlunos
            vagasTotais += vagasDisponiveis
            print(f'Vagas Disponiveis em {turma}: {vagasDisponiveis}')
            contadorDocentes += 1
        contadorVagas += 1
    print(f'Numero total de vagas disponíveis: {vagasTotais}')
    return contadorVagas



def fecharJanela():
    driver.quit()


def main():
    acessarURL()
    driver.implicitly_wait(6)
    selecionarNivelEnsino()
    selecionarUnidade()
    # selecionarSemestre()
    acionarBotaoBuscar()
    contadorVagas = verificaVagas()
    print(f'Numero de turmas encontradas: {contadorVagas/2}')
    fecharJanela()

main()
