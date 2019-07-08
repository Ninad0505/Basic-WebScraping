import requests
from bs4 import BeautifulSoup

url = 'https://www.onefivenine.com/india/BusRouteStage/bus_CityBus_6286_Route.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = soup.find_all('div', class_= "boxinside2")

print(data)

fh = open('demo.txt', 'w+')
fh.write(str(data))




