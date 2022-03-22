import time
import requests
#import pandas as pd
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
#import json


url = "https://sig.unb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino"

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)
time.sleep(6)


#driver.find_element_by_xpath("//*[@id='formTurma:inputDepto']").click()
driver.find_element_by_id("formTurma:inputDepto").click()
driver.find_element_by_xpath('//*[@id="formTurma:inputDepto"]/option[79]').click()
driver.find_element_by_name('formTurma:j_id_jsp_1370969402_11').click()

 

contadorMaterias = 0
element = driver.find_elements_by_class_name('tituloDisciplina')
for k in element:
    html_content = k.get_attribute('innerHTML')
    print(html_content)
    contadorMaterias += 1

print('Total de disciplinas apresentadas na listagem: ', contadorMaterias)

# element1 = driver.find_elements_by_class_name('linhaPar')
# element2 = driver.find_elements_by_class_name('linhaImpar')
# for k in element1:
#     html_content = k.get_attribute('outerHTML')
#     #print(html_content)
#     i += 1
# for k in element2:
#     html_content = k.get_attribute('outerHTML')
#     #print(html_content)
#     i += 1

driver.quit()