# Importando as bibliotecas e módulos necessários para a execução do scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager



# Configurando o driver do navegador
option = Options()
option.headless = True
servicoFirefox = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servicoFirefox, options=option)



# Passando a URL do SIGAA para o Navegador acessar
def acessarURL():
    # Armazenando a URL da página inicial da listagem do SIGAA
    url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"
    driver.get(url)

# Aqui estamos selecionando a opção "Graduação"
def selecionarNivelEnsino():
    botaoCampoEnsino = driver.find_element(By.ID, "formTurma:inputNivel")
    botaoGraduacao = driver.find_element(By.XPATH, '//*[@id="formTurma:inputNivel"]/option[3]')
    botaoCampoEnsino.click()
    botaoGraduacao.click()

# Aqui estamos selecionando o departamento "Faculdade do Gama"
def selecionarUnidade():
    botaoUnidade = driver.find_element(By.ID, "formTurma:inputDepto")
    botaoFGA = driver.find_element(By.XPATH, '//*[@id="formTurma:inputDepto"]/option[79]')
    botaoUnidade.click()
    botaoFGA.click()

# Clicando no botão de busca
def acionarBotaoBuscar():
    botaoBuscar = driver.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11')
    botaoBuscar.click()


def verificaVagas():
    # contadorMaterias armazenará a quantidade de matérias contadas na lista
    contadorMaterias = 0

    # Aqui estamos importando uma lista com todos os títulos de matérias
    # presentes na página do SIGAA
    listaMaterias = driver.find_elements(By.CLASS_NAME, 'tituloDisciplina')

    # Vamos passar por todos os elementos (matérias) da lista de oferta
    # para printar todas elas e contar a quantidade total de matérias
    for materia in listaMaterias:
        nomeMateria = materia.get_attribute('innerHTML')
        print(nomeMateria)
        contadorMaterias += 1
    
    return contadorMaterias


def main():
    acessarURL()

    # Aqui temos uma pausa de 2 segundos para que o navegador carregue as
    # informações necessárias antes de iniciar o scraping
    driver.implicitly_wait(2)

    selecionarNivelEnsino()
    selecionarUnidade()
    acionarBotaoBuscar()

    # Aqui temos uma pausa de 2 segundos para que o navegador carregue as
    # informações necessárias antes de iniciar o scraping
    driver.implicitly_wait(2)

    contMaterias = verificaVagas()
    print('Quantidade de matérias apresentadas na listagem: ', contMaterias)

    # Encerrando o navegador
    driver.quit()

main()