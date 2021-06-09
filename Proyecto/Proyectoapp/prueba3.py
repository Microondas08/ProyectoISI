import requests

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/Rambo"

headers = {
    'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

actor=[]

for i in range(len(response.json()['cast'])):

    actor.insert(i,response.json()['cast'][i]['actor']) 



print(actor)

