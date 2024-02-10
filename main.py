#leia o readme

import requests

def buscar_noticias_palavras_chave(palavras_chave):
    api_key = 'api_do_site_newsapi'
    palavras_query = '+'.join(palavras_chave)
    url = f"https://newsapi.org/v2/everything?q={palavras_query}&apiKey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        links = [article['url'] for article in articles]
        return links
    else:
        print("Erro ao fazer a requisição:", response.status_code)
        return []

def salvar_links_arquivo(links, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        for link in links:
            file.write(link + '\n')

if __name__ == "__main__":
    palavras_chave = input("Digite as palavras-chave para buscar notícias (separadas por vírgula): ").split(',')
    palavras_chave = [palavra.strip() for palavra in palavras_chave]

    links = buscar_noticias_palavras_chave(palavras_chave)

    if links:
        nome_arquivo = input("Digite o nome do arquivo para salvar os links: ")
        salvar_links_arquivo(links, nome_arquivo + ".txt")
        print("Links salvos com sucesso no arquivo", nome_arquivo + ".txt")
    else:
        print("Nenhuma notícia encontrada para as palavras-chave fornecidas.")
