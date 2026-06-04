import re
import threading

import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOBILES = "https://django-anuncios.solyd.com.br/automoveis/"

LINKS = []
NUMBERS = []

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
        description
    )
    
    if regex:
        return regex

def uncover_numbers():
    while True:
        if not LINKS:
            return
        
        link = LINKS.pop(0)
        response_announcement = request(DOMAIN + link)

        if response_announcement:
            soup_announcement = parsing(response_announcement)
            if soup_announcement:
                numbers = find_number(soup_announcement)
                if numbers:
                    for number in numbers:
                        print(f'\nFound telephone number: {number}')
                        NUMBERS.append(number)


if __name__ == '__main__':
    response_search = request(URL_AUTOMOBILES)
    if response_search:
        soup_search = parsing(response_search)
        if soup_search:
            LINKS = find_links(soup_search)
            
            THREADS = []
            for i in range(10):
                thread = threading.Thread(target=uncover_numbers)
                THREADS.append(thread)
            
            for thread in THREADS:
                thread.start()

            for thread in THREADS:
                thread.join()
                
            print(NUMBERS)