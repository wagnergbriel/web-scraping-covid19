from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

class ScrapingCovid19():
    def __init__(self) -> None:
        print("INICIANDO BROWSER")
        chrome_options = ChromeOptions()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.url = "https://covid19br.wcota.me/#tabela"
        # Verifica a versão do navegador e baixa automáticamente
        self.browser = Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=chrome_options)
        self.browser.get(self.url)
    
    def extrair_dados_covid19(self) -> dict:
        try:
            sleep(3)
            print("COLETANDO DOS DADOS, AGUARDE ...")
            tabelas_de_informacoes = self.browser.find_element(By.ID, value="tabela")
            tabelas_de_informacoes.find_element(By.ID, value="total").click()
            sleep(5)
            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            tabela = soup.find("table", id="totalContent-table")
            print(tabela)
        except Exception as e:
            print(e)

ScrapingCovid19().extrair_dados_covid19()


