from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching......\n")
    soup = BeautifulSoup(res.text,'html.parser')  
    location = soup.select('#wob_loc')[20].getText().strip() 
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C") 

city=input("Enter the Name of Any City >>  ")
city=city+" weather"
weather(city)

# import requests
# import json

# def get_weather(api_key, city):
#     base_url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {
#         "q": city,
#         "appid": api_key,
#         "units": "metric"
#     }
    
#     response = requests.get(base_url, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         print("Location:", data["name"])
#         print("Temperature:", data["main"]["temp"], "°C")
#         print("Weather:", data["weather"][0]["description"])
#     else:
#         print("Error occurred:", response.status_code)

# # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
# api_key = 'YOUR_API_KEY'

# # Enter the city for which you want to get the weather update
# city = input("Enter city name: ")

# get_weather(api_key, city)
