from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurar o driver (certifique-se de que o ChromeDriver está no PATH)
driver = webdriver.Chrome()

# Acesse o WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Aguarde o usuário escanear o QR code
input('Pressione Enter depois de escanear o código QR')

def send_message(contact_name, message):
    try:
        # Encontrar a caixa de pesquisa e procurar o contato
        search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(contact_name)
        time.sleep(2)  # Aguarde os resultados aparecerem

        # Selecionar o contato
        contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
        contact.click()

        # Encontrar a caixa de mensagem e enviar a mensagem
        message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)

    except Exception as e:
        print(f'Erro: {e}')

def handle_response(contact_name, message):
    if 'cabelo' in message.lower():
        send_message(contact_name, 'Você escolheu Cabelo. Por favor, aguarde enquanto preparamos um atendimento.')
    elif 'barba' in message.lower():
        send_message(contact_name, 'Você escolheu Barba. Por favor, aguarde enquanto preparamos um atendimento.')
    elif 'pagamento' in message.lower():
        send_message(contact_name, 'Você escolheu Gerar Pagamento. Por favor, aguarde enquanto geramos o pagamento.')
    else:
        send_message(contact_name, 'Opção inválida. Por favor, escolha 1 para Cabelo, 2 para Barba ou 3 para Pagamento.')

def send_initial_message(contact_name):
    message = (
        'Olá! Bem-vindo à nossa barbearia. Por favor, escolha uma opção:\n'
        '1. Cabelo\n'
        '2. Barba\n'
        '3. Gerar Pagamento'
    )
    send_message(contact_name, message)

# Exemplo de uso
contact_name = 'Nome do Contato'

# Enviar mensagem inicial
send_initial_message(contact_name)

# Simular uma resposta do usuário
# Aqui você deve incluir a lógica para processar mensagens recebidas
# Isso geralmente requer monitoramento contínuo, o que não é simples com Selenium

# Exemplo de resposta
response = input('Digite a resposta simulada do usuário: ')
handle_response(contact_name, response)

# Fechar o navegador
driver.quit()
