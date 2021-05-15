from django.shortcuts import render,  redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
import pandas as pd

# Create your views here.

def index(request):

   return render(request, "home.html")

def busqueda(request):


   url = "https://google-search3.p.rapidapi.com/api/v1/serp/"

   payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
   headers = {
      'content-type': "application/json",
      'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
      'x-rapidapi-host': "google-search3.p.rapidapi.com"
      }

   response = requests.request("POST", url, data=payload, headers=headers)

   print(response.text)

   return (response, "busqueda.html", {})

    
