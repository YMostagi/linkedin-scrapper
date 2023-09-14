# linkedin-scrapper

# Script para coletar links de perfis do LinkedIn em um fórum

Esse script em Python utiliza a biblioteca requests e a biblioteca BeautifulSoup para navegar por um fórum de internet, coletar os links dos perfis do LinkedIn postados pelos usuários e salvá-los em um arquivo .csv.

## Funcionamento do script

O script começa definindo a URL do fórum, o número de páginas que deseja percorrer e o nome do arquivo .csv onde serão salvos os links dos perfis do LinkedIn. É necessário que o usuário especifique esses valores no próprio script antes de executá-lo.

Em seguida, o script inicia a inicialização do arquivo .csv com o cabeçalho. Depois, o script percorre cada página do fórum, extrai os links dos perfis do LinkedIn usando BeautifulSoup e salva-os no arquivo .csv.

## Documentação

### Requisitos

Para executar o script, é necessário ter o Python 3 instalado no computador, bem como as bibliotecas requests e BeautifulSoup. Elas podem ser instaladas utilizando os seguintes comandos no terminal:

```bash
pip install requests
pip install beautifulsoup4
```

### Como executar

1. Abra o arquivo `script.py` em um editor de texto.
2. Modifique as variáveis `url`, `numero_de_paginas` e `nome_arquivo_csv` de acordo com o fórum que deseja coletar os links dos perfis do LinkedIn e o nome que deseja dar ao arquivo .csv que será gerado.
3. Salve as modificações no arquivo.
4. Abra um terminal na pasta onde está o arquivo `script.py`.
5. Digite o comando `python script.py` e pressione Enter.

### Saída

O script irá percorrer todas as páginas do fórum especificado, extrair os links dos perfis do LinkedIn postados pelos usuários e salvá-los no arquivo .csv especificado. Ao final, uma mensagem será exibida informando que os links dos perfis do LinkedIn foram salvos no arquivo especificado.

## Licença

Esse script é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
