import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/Rambo"

headers = {
    'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

actor=[]



for i in range(len(response.json()['cast'])):

    actor.insert(i,response.json()['cast'][i]['actor']) 


url='https://www.cinesa.es/peliculas/cartelera'

page = requests.get(url)

soup= BeautifulSoup(page.content, 'html.parser')

pelicula = soup.find_all('a', class_='vf')

peliculas = list()


count = 0
for i in pelicula: 
    if count < 20:
        if count % 2 == 0:
            peliculas.append(i.text)
    else:
        break

    count+=1

print(peliculas) 



