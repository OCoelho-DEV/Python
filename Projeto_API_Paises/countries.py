import json

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
            print(f'Can not access: {status_code}')
    except:
        print('Error at request:', url)

def parsing(response_text):
    try:
        return json.loads(response_text)
    except:
        print('Error at parsing text')

def countries_count(countries_list):
    return len(countries_list)

def list_countries(countries_list):
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
            print(f"{country['name']['common']}: {country['population']:,}")

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

if __name__ == '__main__':
    # response_text = request(URL_ALL)
    # if response_text:
    #     countries_list = parsing(response_text)
    #     if countries_list:
    #         countries_count(countries_list)
    #         list_countries(countries_list)
    #         show_population('brazil')
    # show_population('usa')
    show_currencies('bra')