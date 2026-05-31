import requests

URL_NAME = 'https://restcountries.com/v3.1/name/brazil'
URL_ALL = 'https://restcountries.com/v3.1/all?fields=name,capital,currencies'
response = requests.get(URL_ALL)
response2 = requests.get(URL_NAME)
print(response2.text)