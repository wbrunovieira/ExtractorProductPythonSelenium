from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configurações do navegador e Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Rodar em background
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')
# Adicionar o header na requisição
chrome_options.add_argument('user-agent=Seu User Agent Aqui')

# Caminho para o seu WebDriver
driver_path = 'caminho/para/o/seu/webdriver'

# Inicializando o WebDriver com as opções definidas
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# URL do site alvo
url = 'https://www.liz.com.br/calcinhas'

# Acessar o site
driver.get(url)

# Agora você pode começar a extrair as informações...
