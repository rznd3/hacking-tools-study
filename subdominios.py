import requests

url = 'terra.com.br'

file = open('subdomains-top1million-5000.txt')

# percorrendo wordlist
for line in file:
    line = line.strip()
    
    # monta url
    sub_to_check = f'https://{line}.{url}'

    try:
        r = requests.get(sub_to_check)
        print('sucesso')
        print(sub_to_check)
        print('---------------------')

    except:
        print(f'error {sub_to_check}')
        print('---------------------')

        continue

    
