import requests

url = 'https://www.bbc.co.uk/'

list = ['admin', 'login', 'css', 'sport']

for i in list:

    url_to_check = url + i
    r = requests.get(url_to_check)

    if r.status_code == 200:
        print(url_to_check)
        print(r.status_code)
        print('---------------------')

    else:
        print('its not 200')
        print('---------------------')

    
