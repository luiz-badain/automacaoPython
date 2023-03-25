from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

#acessar o site do connect
navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://connect-positivo.navita.com.br/")

#login
navegador.find_element("xpath", '//*[@id="username"]').send_keys("luiz.costa")
navegador.find_element("xpath", '//*[@id="password"]').send_keys("1234")
navegador.find_element("xpath", '//*[@id="kc-login"]').click()

time.sleep(7)

# acessando empresa
navegador.find_element("xpath", '//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a/label').click() 
time.sleep(5)
navegador.find_element("xpath", '//*[@id="input"]').send_keys("SERTAOZINHO")
time.sleep(3)
navegador.find_element("xpath", '//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(6)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")

time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[4]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)


#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(7)


                            ########################### SOROCABA #########################

# acessando empresa
#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("SOROCABA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

########################### SUL 1  #########################

# acessando empresa
#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("SUL 1")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


########################### SUL 2 #########################

# acessando empresa
#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("SUL 2")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

########################### SUL 3 #########################

# acessando empresa
#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("SUL 3")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


                ########################### SUMARE #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("SUMARE")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### SUZANO #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("SUZANO")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

    ########################### TABOAO DA SERRA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("TABOAO DA SERRA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

    ########################### TAQUARITINGA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("TAQUARITINGA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### TAUBATE #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("TAUBATE")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### TUPA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("TUPA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

    ########################### VOTORANTIM #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("VOTORANTIM")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### VOTUPORANGA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("VOTUPORANGA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### APIAI #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("APIAI")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### ARARAQUARA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("ARARAQUARA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### ASSIS #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("ASSIS")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### AVARE #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("AVARE")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

    ########################### BARRETOS #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("BARRETOS")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### BOTUCATU #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("BOTUCATU")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### CAIEIRAS #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CAIERAS")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

    ########################### CAMPINAS OESTE #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CAMPINAS OESTE")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### CAPIVARI #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CAPIVARI")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### CARAPICUIBA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CARAPICUIBA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### CATANDUVA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CATANDUVA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### CENTRO #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CENTRO")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### CENTRO OESTE #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("CENTRO OESTE")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

    ########################### DIADEMA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("DIADEMA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### FERNANDOPOLIS #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("FERNANDOPOLIS")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### FRANCA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("FRANCA")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)


    ########################### GUARATINGUETA #########################


#Acessar o Ambiente Criado
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/a').click()
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
navegador.find_element("xpath",'//*[@id="input"]').send_keys("GUARATINGUETA ")
time.sleep(5)
navegador.find_element("xpath",'//*[@id="body-portal"]/header/div/div/nav/ul/li[2]/ul/li/ul/li/span[1]/a/span').click()
time.sleep(5)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)

#app Centro de Mídias SP 
time.sleep(2)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[24]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_UP)
time.sleep(2)

#filtro para mostrar 50
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/button').click()
time.sleep(1)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[1]/div/ul/li[4]/button').click()
time.sleep(2)


#app minha escola
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[1]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app diario de classe
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[2]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Kidle
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[4]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app chrome
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[5]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app classroom
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[8]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app drive
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[9]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Documentos
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[10]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app planilhas
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[11]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Apresentações 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[12]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Chat
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[13]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(5)

#app Jamboard
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[14]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Meet
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[15]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Google Agenda
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[16]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)

#app Gmail 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[17]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Google Keep 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[18]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Acessibilidade 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[19]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[2]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Voice leia em voz alta
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[20]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)

#app Teams
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[21]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)

#app Leitor Resposta 
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/section/div[3]/div[2]/div[1]/table/tbody/tr[22]/td[6]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div[2]/section/div/div/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
navegador.find_element("xpath", '//*[@id="content-page"]/div/div/div/div[2]/div[2]/div/div/button').click()
time.sleep(60)
navegador.get("https://connect-positivo.navita.com.br/portal/#/emm/apps/catalog/ANDROID")
time.sleep(10)
navegador.find_element("xpath", '/html/body').send_keys(Keys.PAGE_DOWN)
time.sleep(5)












































