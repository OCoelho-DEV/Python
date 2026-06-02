import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOBILES = "https://django-anuncios.solyd.com.br/automoveis/"

def search(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f'Not found: {response.status_code}')
    except Exception as error:
        print('Error at request')
        print(error)

def parsing(response_html):
    try:
        soup = BeautifulSoup(response_html, 'html.parser')
        return soup
    except Exception as error:
        print('Error at parsing html:', error)

def find_links(soup):
    cards_parent = soup.find('div', class_='ui three doubling link cards')
    cards = cards_parent.find_all('a')

    links = []
    for card in cards:
        link = card['href']
        links.append(link)

    return links

response = search(URL_AUTOMOBILES)

if response:
    soup = parsing(response)
    if soup:
        links = find_links(soup)
        print(links)
    
