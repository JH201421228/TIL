API_KEY = '356d53a5bbb7dcc61a7e0be4154706c5'
lat = 37.56
lon = 126.97
city_name = 'Seoul,KR'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

import requests
# API 요청 보내기
response = requests.get(url).json()
temp = response['main']['temp'] - 273.15
print(temp)
print(response)