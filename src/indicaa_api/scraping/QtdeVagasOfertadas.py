from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys



option = Options()
option.headless = True
servicoFirefox = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servicoFirefox, options=option)


def acessarURL():
    url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"
    driver.get(url)


def selecionarNivelEnsino():
    botaoCampoEnsino = driver.find_element(By.ID, 'formTurma:inputNivel')
    botaoGraduacao = driver.find_element(By.XPATH, '//*[@id="formTurma:inputNivel"]/option[3]')
    botaoCampoEnsino.click()
    botaoGraduacao.click()

def selecionarSemestre():    
    inputAno = driver.find_element(By.ID, "formTurma:inputAno")
    inputAno.click()
    inputAno.send_keys(Keys.CONTROL, 'a')
    inputAno.send_keys('2021')
    botaoSemestre=driver.find_element(By.XPATH, '//*[@id="formTurma:inputPeriodo"]/option[2]')
    botaoSemestre.click()

def selecionarUnidade():
    botaoUnidade = driver.find_element(By.ID, 'formTurma:inputDepto')
    botaoFGA = driver.find_element(By.XPATH, '//*[@id="formTurma:inputDepto"]/option[79]')
    botaoUnidade.click()
    botaoFGA.click()


def acionarBotaoBuscar():
    botaoBuscar = driver.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11')
    botaoBuscar.click()


def verificaVagasOfertadas():
    contadorDocentes = 0
    contadorVagas = 0
    element1 = driver.find_elements(By.XPATH, "//td[@style='text-align: center;']")
    for x in element1:
        resto = contadorVagas % 2
        vagasOfertadas = x.get_attribute('innerHTML')
        if resto == 0: 
            disciplina = driver.find_elements(By.XPATH, "//td[@class='nome']")[contadorDocentes]
            turma = disciplina.get_attribute('innerHTML')
            print(f'Vagas Ofertadas em {turma}: {vagasOfertadas}')
            contadorDocentes += 1
        contadorVagas += 1
    return contadorVagas


def fecharJanela():
    driver.quit()



def main():
    acessarURL()
    driver.implicitly_wait(6)
    selecionarNivelEnsino()
    selecionarUnidade()
    selecionarSemestre()
    acionarBotaoBuscar()
    contadorVagas = verificaVagasOfertadas()
    print(f'Numero de Turmas encontradas: {contadorVagas/2}')
    fecharJanela()


main()
