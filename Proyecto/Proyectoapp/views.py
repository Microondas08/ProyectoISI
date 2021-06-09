from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import pandas as pd

# Create your views here.

def index(request):

   return render(request, "home.html")

def pelicula(request):

   if request.GET.get('busqueda'):

      busqueda = request.GET.get('busqueda')


      url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/" + busqueda

      headers = {
         'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
         'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
         }

      response = requests.request("GET", url, headers=headers)

      actor=[]

      for i in range(len(response.json()['cast'])):

         actor.insert(i,response.json()['cast'][i]['actor']) 

      
      rating = response.json()['rating']
      length = response.json()['length']

      

      url = "https://google-search3.p.rapidapi.com/api/v1/images/q=" + busqueda

      payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
      headers = {
         'content-type': "application/json",
         'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
         'x-rapidapi-host': "google-search3.p.rapidapi.com"
         }

      response = requests.request("GET", url, data=payload, headers=headers)


      foto=response.json()["image_results"][1]["image"]["src"]

      return render(request, "pelicula.html", {'actor': actor, 'rating':rating, 'length':length, 'foto':foto})



   return render(request, "pelicula.html")

def busqueda(request):

   if request.GET.get('busqueda'):

   
      busqueda = request.GET.get('busqueda')

      print(busqueda)


      url = "https://google-search3.p.rapidapi.com/api/v1/images/q=" + busqueda

      payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
      headers = {
         'content-type': "application/json",
         'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
         'x-rapidapi-host': "google-search3.p.rapidapi.com"
         }

      response = requests.request("GET", url, data=payload, headers=headers)


      foto=response.json()["image_results"][1]["image"]["src"]
      

      url = "https://google-search3.p.rapidapi.com/api/v1/search/q=" + busqueda

      headers = {
         'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
         'x-rapidapi-host': "google-search3.p.rapidapi.com"
         }

      response = requests.request("GET", url, headers=headers)

      info1title = response.json()["results"][1]["title"]
      info1link = response.json()["results"][1]["link"]

      info2title = response.json()["results"][2]["title"]
      info2link = response.json()["results"][2]["link"]

      info3title = response.json()["results"][3]["title"]
      info3link = response.json()["results"][3]["link"]


      return render(request, "busqueda.html", {'foto': foto, 'info1title': info1title, 'info1link':info1link, 'info2title': info2title, 'info2link':info2link, 'info3title': info3title, 'info3link':info3link})

   return render(request, "busqueda.html")

    
