from gettext import gettext
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def acessarURL():
    url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"
    driver.get(url)


def selecionarNivelEnsino():
    botaoCampoEnsino = driver.find_element_by_id('formTurma:inputNivel')
    botaoGraduacao = driver.find_element_by_xpath('//*[@id="formTurma:inputNivel"]/option[3]')
    botaoCampoEnsino.click()
    botaoGraduacao.click()


def selecionarUnidade():
    botaoUnidade = driver.find_element_by_id('formTurma:inputDepto')
    botaoFGA = driver.find_element_by_xpath('//*[@id="formTurma:inputDepto"]/option[79]')
    botaoUnidade.click()
    botaoFGA.click()


def acionarBotaoBuscar():
    botaoBuscar = driver.find_element_by_name('formTurma:j_id_jsp_1370969402_11')
    botaoBuscar.click()


def verificaVagas():
    contadorDocentes = 0
    contadorVagas = 0
    element1 = driver.find_elements_by_xpath("//td[@style='text-align: center;']")
    for x in element1:
        resto = contadorVagas % 2
        html_content = x.get_attribute('innerHTML')
        if resto == 1: 
            disciplina = driver.find_elements_by_xpath("//td[@class='nome']")[contadorDocentes]
            turma = disciplina.get_attribute('innerHTML')
            print(f'Vagas em {turma}: {html_content}')
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
    acionarBotaoBuscar()
    contadorVagas = verificaVagas()
    print(f'Numero de Turmas encontradas: {contadorVagas/2}')
    fecharJanela()


main()