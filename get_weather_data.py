
import requests
city_name = input("Enter the city name:")
API_Key = '746e9b83fc5bb252ce82458e9515b4a3'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is',data['weather'][0]['description'])
    print('Current Temperature is',data['main']['temp'])
    print('Current Temperature feels like is',data['main']['feels_like'])
    print('Humidity is',data['main']['humidity'])
else:
    print(f"Error {response.status_code}: Unable to retrieve weather data.")




    

    

    

    

