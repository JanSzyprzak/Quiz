import requests
from django.shortcuts import render

# Create your views here.




def get_data(request):
    url = 'https://opentdb.com/api.php?amount=10&category=22&difficulty=easy'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        return None

