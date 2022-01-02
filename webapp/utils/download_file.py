from typing import List
import requests
import os
from bs4 import BeautifulSoup


def element_finder(txt : str, elements : List):
    for element in elements:
        if txt in element.text:
            return element

    return None

def download_files() -> bool:
    url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/vendas-de-derivados-de-petroleo-e-biocombustiveis'
    url_main_file = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-estatisticos/de/vdpb/vendas-combustiveis-m3-1.xls/view'

    req = requests.get(url)
    page_source = req.content

    soup = BeautifulSoup(page_source, 'html.parser')

    #Coleta todas as tags A
    a_tags = soup.select('a.internal-link')
    #Procura dentro das tags qual corresponde ao texto desejado
    try:
        vendas_combs_link = element_finder('Vendas de derivados petróleo e etanol (metros cúbicos)', a_tags)['href']
        vendas_diesel_link = element_finder('Vendas de óleo diesel por tipo (metros cúbicos)', a_tags)['href']
    except TypeError:
        return False

    link_list = [vendas_diesel_link, vendas_combs_link]
    try:
        os.mkdir('./csv_files')
    except FileExistsError:
        pass
    #Inicia o download dos arquivos csv
    for index, link in enumerate(link_list):
        download_req = requests.get(link, allow_redirects=True)
        open(f'./csv_files/data_source{index}.csv', 'wb').write(download_req.content)

    #Request para a URL que contém a planilha principal
    req = requests.get(url_main_file)
    page_source = req.content

    soup = BeautifulSoup(page_source, 'html.parser')
    
    link_main_file = soup.select('div#content-core > p > a')[0]['href']
    #Incia do download da planilha pricipal .xls
    if link_main_file is not None:
        download_req = requests.get(link_main_file)
        open(f'./csv_files/vendas-combustiveis-m3.xls', 'wb').write(download_req.content)
    else:
        return False
    return True
