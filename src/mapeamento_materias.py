# Importando as bibliotecas e módulos necessários para a execução do scraping
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Armazenando a URL da página inicial da listagem do SIGAA
url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"

# Configurando o driver do navegador e passando a URL do SIGAA para ele
option = Options()
option.headless = True
servicoFirefox = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servicoFirefox, options=option)
driver.get(url)

# Aqui temos uma pausa de 2 segundos para que o navegador carregue as
# informações necessárias antes de iniciar o scraping
time.sleep(2)

# Aqui estamos selecionando a opção "Graduação"
driver.find_element(By.ID, "formTurma:inputNivel").click()
driver.find_element(By.XPATH, '//*[@id="formTurma:inputNivel"]/option[3]').click()

# Aqui estamos selecionando o departamento "Faculdade do Gama"
driver.find_element(By.ID, "formTurma:inputDepto").click()
driver.find_element(By.XPATH, '//*[@id="formTurma:inputDepto"]/option[79]').click()

# Clicando no botão de busca
driver.find_element(By.NAME, 'formTurma:j_id_jsp_1370969402_11').click()

# Aqui temos uma pausa de 2 segundos para que o navegador carregue as
# informações necessárias antes de iniciar o scraping
time.sleep(2)

# contadorMaterias armazenará a quantidade de matérias contadas na lista
contadorMaterias = 0

# Aqui estamos importando uma lista com todos os títulos de matérias
# presentes na página do SIGAA
element = driver.find_elements(By.CLASS_NAME, 'tituloDisciplina')

# Vamos passar por todos os elementos (matérias) da lista de oferta
# para printar todas elas e contar a quantidade total de matérias
for k in element:
    html_content = k.get_attribute('innerHTML')
    print(html_content)
    contadorMaterias += 1

print('Quantidade de matérias apresentadas na listagem: ', contadorMaterias)

# Encerrando o navegador
driver.quit()