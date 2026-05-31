import json
import sys

import requests

URL_NAME = 'https://restcountries.com/v3.1/name/'
URL_ALL = 'https://restcountries.com/v3.1/all?fields=name,capital,currencies'
# response = requests.get(URL_ALL)
# response2 = requests.get(URL_NAME)

# countries = json.loads(response.text)
# print(countries[-1]['name']['common'])
# print(len(countries))
# for country in countries:
#     print(country['name']['common'], country['currencies'])

def request(url):
    try:
        response = requests.get(url)
        status_code = response.status_code

        if status_code == 200:
            return response.text
        else:
            print(f'Not found: {status_code}')
    except:
        print('Error at request:', url)

def parsing(response_text):
    try:
        return json.loads(response_text)
    except:
        print('Error at parsing text')

def countries_count(countries_list=None):
    response = request(URL_ALL)
    if response:
        countries_list = parsing(response)
        if countries_list:
            return len(countries_list)

def list_countries(countries_list=None):
    response = request(URL_ALL)
    if response:
        countries_list = parsing(response)
        if countries_list:
            for country in countries_list:
                print(country['name']['common'])

def show_population(country_name):
    response = request(f'{URL_NAME}{country_name}')
    if response:
        countries_list = parsing(response)
        if not countries_list:
            print('Country not found')
            return
        
        for country in countries_list:
            print(f"{country['name']['common']}: {country['population']:,}"
                  " inhabitants")

def show_currencies(country_name):
    response = request(f'{URL_NAME}{country_name}')
    if response:
        countries_list = parsing(response)
        if not countries_list:
            print('Country not found')
            return
        
        for country in countries_list:
            currencies = country['currencies']
            print(f"{country['name']['common']} currencies:")
            for code, currency_data in currencies.items():
                print(f"{currency_data['name']} - {code}")

def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print('Is necessary to pass the country name on'
        ' <country name>')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('## Welcome at countries system!')
        print('Usage: python Projeto_API_Paises/countries.py'
        ' <action> <country name>')
        print('Actions: Count, Currency, Population, List')
    else:
        arg1 = sys.argv[1]
        match arg1.lower():
            case 'count':
                countries_number = countries_count()
                print(f'Exists {countries_number} countries in the world!')
            case 'currency':
                country_name = read_country_name()
                if country_name:
                    show_currencies(country_name)
            case 'population':
                country_name = read_country_name()
                if country_name:
                    show_population(country_name)
            case 'list':
                list_countries()
            case _:
                print('Invalid Argument')