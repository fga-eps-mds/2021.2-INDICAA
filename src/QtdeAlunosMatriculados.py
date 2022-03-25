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
driver.find_element_by_id("formTurma:inputNivel").click()
driver.find_element_by_xpath('//*[@id="formTurma:inputNivel"]/option[3]').click()

driver.find_element_by_id("formTurma:inputDepto").click()
driver.find_element_by_xpath('//*[@id="formTurma:inputDepto"]/option[79]').click()
driver.find_element_by_name('formTurma:j_id_jsp_1370969402_11').click()

 


contadorVagas = 0
element1 = driver.find_elements_by_xpath("//td[@style='text-align: center;']")
for x in element1:
    resto = contadorVagas % 2
    html_content = x.get_attribute('innerHTML')
    if resto == 1: 
        print(html_content)
    contadorVagas += 1

print('Numero de Vagas encontradas', contadorVagas/2)

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
