import os
import requests
from bs4 import BeautifulSoup
import csv

# URL do fórum
url = 'https://exemplo.com/forum'

# Número de páginas do fórum que você deseja percorrer
numero_de_paginas = 5

# Nome do arquivo csv onde serão salvos os links dos perfis do LinkedIn
nome_arquivo_csv = 'links_perfil_linkedin.csv'

# Cabeçalho do arquivo csv
cabecalho_csv = ['nome', 'perfil_linkedin']

# Obtém o separador de diretórios do sistema operacional
separador_diretorios = os.path.sep

# Obtém o caminho completo para o arquivo csv
caminho_completo_arquivo_csv = '.' + separador_diretorios + nome_arquivo_csv

# Inicializa o arquivo csv com o cabeçalho
with open(caminho_completo_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(cabecalho_csv)

# Percorre cada página do fórum
for i in range(1, numero_de_paginas+1):

    # URL da página atual
    url_pagina_atual = url + '?pagina=' + str(i)

    # Faz a requisição GET na página atual do fórum
    resposta = requests.get(url_pagina_atual)

    # Extrai os links dos perfis do LinkedIn usando BeautifulSoup
    soup = BeautifulSoup(resposta.content, 'html.parser')
    links_perfil_linkedin = [a['href'] for a in soup.find_all('a', href=True) if 'linkedin.com/in/' in a['href']]

    # Salva os links dos perfis do LinkedIn no arquivo csv
    with open(caminho_completo_arquivo_csv, 'a', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for link in links_perfil_linkedin:
            # Extrai o nome do perfil do LinkedIn
            nome_perfil = link.split('/')[-1]
            escritor_csv.writerow([nome_perfil, link])

print('Links dos perfis do LinkedIn salvos em', caminho_completo_arquivo_csv)
