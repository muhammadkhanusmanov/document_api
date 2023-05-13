import requests

url='http://127.0.0.1:8000/do/1222'

try:
    with open('l.docx', 'rb') as file:
        response = requests.post(url, files={'file': file})
        response.raise_for_status()
        print(response.json())
except requests.exceptions.RequestException as e:
    print('Error:', e)