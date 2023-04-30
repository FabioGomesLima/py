from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Inicialize o driver do Chrome
driver = webdriver.Chrome()

# Navegue até a página do WhatsApp
driver.get("https://web.whatsapp.com/")

# Espere o usuário fazer login no WhatsApp Web
input("Faça login no WhatsApp Web e pressione enter")

# Nome do contato a ser monitorado
contato_monitorado = "Amor"

# Localize o contato na lista de bate-papos
contato = driver.find_element_by_xpath(f'//span[@title="{8481493887}"]')

# Clique no contato para abrir a conversa
contato.click()

# Encontre a caixa de entrada de mensagem
caixa_de_texto = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')

# Encontre a mensagem mais recente no chat
mensagem_atual = driver.find_elements_by_css_selector("div[class='_1Gy50'] span.selectable-text")[-1].text

# Loop infinito para monitorar novas mensagens
while True:
    # Verifique se há uma nova mensagem
    mensagem_nova = driver.find_elements_by_css_selector("div[class='_1Gy50'] span.selectable-text")[-1].text
    
    # Se a mensagem atual for diferente da nova mensagem, responda automaticamente
    if mensagem_nova != mensagem_atual:
        # Atualize a mensagem atual
        mensagem_atual = mensagem_nova
        
        # Digite a mensagem de resposta na caixa de texto
        mensagem_resposta = "Olá, recebemos sua mensagem! Vamos responder o mais rápido possível."
        caixa_de_texto.send_keys(mensagem_resposta)
        
        # Pressione enter para enviar a mensagem
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.CONTROL).perform()
        
    # Aguarde 1 segundo antes de verificar novamente
    time.sleep(1)
