import re

import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOBILES = "https://django-anuncios.solyd.com.br/automoveis/"

def request(url):
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
    try:
        cards_parent = soup.find('div', class_='ui three doubling link cards')
        cards = cards_parent.find_all('a')
    except:
        print('Error at find cards on link')

    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            pass
    return links

def find_number(soup):
    try:
        description = soup.find_all('div', class_='sixteen wide column')[2].p.\
            get_text().strip()
    except:
        print('Error as find href description')
        return
    
    regex = re.findall(
        r'\(?0?([1-9]{2})[ \-\.\)]{0,2}(9?[ \-\.]?\d{4})[ \-\.]?(\d{4})',
        description)
    
    if regex:
        return regex

response_search = request(URL_AUTOMOBILES)

if response_search:
    soup_search = parsing(response_search)
    if soup_search:
        links = find_links(soup_search)
        for link in links:
            response_announcement = request(DOMAIN + link)
            if response_announcement:
                soup_announcement = parsing(response_announcement)
                if soup_announcement:
                    number = find_number(soup_announcement)
                    print(number)

