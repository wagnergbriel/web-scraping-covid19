from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

class ScrapingCovid19():
    def __init__(self) -> None:
        print("INICIANDO BROWSER")
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.url = "https://covid19br.wcota.me/#tabela"
        # Verifica a versão do navegador e baixa automáticamente
        # Caso seu browser não seja o que está configurado, acesse o link abaixo 
        # para modificar de acordo com o browser da sua máquina:
        # https://pypi.org/project/webdriver-manager/
        self.browser = Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)
        self.browser.get(self.url)

    def extrair_dados_covid19(self) -> dict:
        try:
            sleep(3)
            print("COLETANDO OS DADOS, AGUARDE ...")
            tabelas_de_informacoes = self.browser.find_element(By.ID, value="tabela")
            tabelas_de_informacoes.find_element(By.ID, value="total").click()
            sleep(3)
            soup = BeautifulSoup(self.browser.page_source, 'html.parser')
            tabela = soup.find("table", id="totalContent-table")
            colunas =  list(map(lambda tag: tag.get_text(), tabela.find_all("th")))
            bloco_de_linhas = tabela.find_all("tr") #list(map(lambda tag: tag, tabela.find_all("tr")))
            lista_de_dados = self.__coletar_dados_da_tabela(bloco_de_linhas[1:])
            #print(lista_de_dados)
            #print(list({coluna: dado for coluna, dado in zip(colunas, lista_de_dados)}))
            print(self.__lista_de_dict_covid(colunas, lista_de_dados))
        except Exception as e:
            print(e)
    
    def __coletar_dados_da_tabela(self, lista_de_dados: list) -> list:
            lista_dados_por_linha = []
            for linha in lista_de_dados:
                lista_dados_por_linha.append(
                        list(map(lambda tag: tag.get_text(), linha.find_all("td")))
                )
            return lista_dados_por_linha
    
    def __lista_de_dict_covid(self, colunas, lista_de_dados):
        lista_de_dict = []
        for dado in lista_de_dados:
            print(dado)
            #lista_de_dict.append({coluna: dado})
        #return lista_de_dict
    
    def gerar_csv(self) -> None:
        self.extrair_dados_covid19()
                

covid = ScrapingCovid19()
covid.extrair_dados_covid19()
#covid.gerar_csv()


