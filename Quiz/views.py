import requests
import random
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session



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

        request.session['questions'] = data['results']

        return render(request, 'Quiz/data.html', {'data': data})
    else:
        return render(request, 'Quiz/data.html', {'data': None})
    

def submit_answers(request):
    if request.method == 'POST':
        points = 0
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_index = int(key.split('_')[1]) - 1
                selected_answer = value

                question_data = request.session['questions'][question_index]
                correct_answer = question_data['correct_answer']
                difficulty = question_data['difficulty']

                if selected_answer == correct_answer:
                    if difficulty == 'easy':
                        points += 1
                    elif difficulty == 'medium':
                        points += 2
                    elif difficulty == 'hard':
                        points += 3

        request.session['points'] = points
        return redirect('Quiz:result')
    else:
        return redirect('Quiz:fetch_data')
    

def result(request):
    points = request.session.get('points', None)
    if points is not None:
        del request.session['points']
        return render(request, 'Quiz/result.html', {'points': points})
    else:
        return redirect('Quiz:fetch_data')