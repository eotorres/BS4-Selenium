#Imports das librarys para execução
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests

#Definição e conexão do driver/web
driver = webdriver.Chrome()
url = "http://web.whatsapp.com"
driver.get(url)
print('O bot (nome de sua escolhas) irá se iniciar em 10 segundos apos a leitura do QrCode')
time.sleep(10)

#Definição das Mensagens
reply = "Mensagem a sua escolha, para todos os contatos"
reply_grupo = 'Mensagem somente para grupos'
reply_contato_avulso = 'Mensagem para contato que o bot irá localizar '

#Definição dos Grupos
groups = ["Nome do grupo"]

#Denifição dos Contatos Avulsos
contato_contato = ['Nome do Contato que será buscado']


#Definição dos arquivos de imagens para envio
photo_path = "Local da imagem"

###########################################################################################################################
#Buscando contato avulsos por definição, por nome validando se já houve conversa
for user_contato in contato_contato:
            user_contato_avulso = driver.find_element_by_xpath(f'//span[@title="{user_contato}"]')
            time.sleep(3)
            user_contato_avulso.click()
            msg_box = driver.find_element_by_class_name('_3uMse')
            time.sleep(5)
            msg_box.click()
            msg_box.send_keys(reply_contato_avulso)
            btn_enviar = driver.find_element_by_class_name('_1U1xa')
            time.sleep(3)
            btn_enviar.click()
            time.sleep(3)

#---------- Implantar envio de imagens -----------------------------------------------------------------------------------#
            image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys(photo_path)
            send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
            send_button.click()
#-------------------------------------------------------------------------------------------------------------------------#
            
###########################################################################################################################
#Validando mensagens recebidas para criação das respostas
while True:
    time.sleep(10)
    res = driver.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(res, "lxml")
    contacts = soup.find_all('div', {'class': '_210SC'}) #classe das filhas(leitura de todas as conversas)
    print(len(contacts))

#Leitura dos contatos, para a contagem de mensagens sem respostas
    for contact in contacts:
        contact_name = contact.find('span', {'class': '_3ko75 _5h6Y_ _3Whw5'}).text.replace("\n", "").strip() 
        try:
            msg_count = contact.find('span', {'class': '_31gEB'}).text.replace("\n", "").strip()
        except:
            msg_count = 0   

#If validando as mensagens com base nas mensagens para ser respondidas  
#Aqui descarto os grupos, validando somente os contatos   
        if int(msg_count) > 0 and contact_name not in groups:
            try:
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(contact_name))
                user.click()
                time.sleep(3)
                msg_box = driver.find_element_by_class_name('_3uMse')
                msg_box.send_keys(reply)
                driver.find_element_by_class_name('_1U1xa').click()
                lista_mensagens_enviadas.append(user,msg_box,user_contato_avulso)
            except:
                pass
        print(contact_name, msg_count)
            

   


            
        
        
        
  

        

        
        
        
       



