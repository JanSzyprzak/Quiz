import requests
import random
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def fetch_data(request):
    url = 'https://opentdb.com/api.php?amount=10'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for question in data['results']:
            answers = question['incorrect_answers']
            answers.append(question['correct_answer'])
            random.shuffle(answers)
            question['mixed_answers'] = answers

        return render(request, 'Quiz/data.html', {'data': data})
    else:
        return render(request, 'Quiz/data.html', {'data': None})