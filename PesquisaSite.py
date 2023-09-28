import requests
from bs4 import BeautifulSoup


site_alvo = input("Digite o site que você deseja pesquisar: ")


url_pesquisa = f"https://whois.domaintools.com{site_alvo}"


response = requests.get(url_pesquisa)


if response.status_code == 200:
   
    soup = BeautifulSoup(response.text, "html.parser")

    
    titulo = soup.find("h3").text

    
    print(f"Site pesquisado: {site_alvo}")
    print(f"Título do site encontrado nos resultados: {titulo}")
else:
    print(f"Não foi possível acessar o site de pesquisa. Código de status: {response.status_code}")