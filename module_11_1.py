import requests
url ='https://www.example.com/'
response=requests.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print('Ошибка:', response.status_code)



url2 = 'https://www.example.com/api/data'
data2 = {'key1': 'value1', 'key2': 'value2'}
response2 = requests.post(url2, data=data2)

if response2.status_code == 200:
    print(response2.json())
else:
    print('Ошибка:', response2.status_code)

url3 = 'https://www.example.com'
headers3 = {'User-Agent': 'My Custom User Agent'}
response3 = requests.get(url3, headers=headers3)

print(response3.headers)
