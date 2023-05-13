import requests
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth import login
from . models import LeaderboardEntry
from . forms import RegistrationForm
from .forms import QuizConfigForm

# Create your views here.



@login_required
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
    
@login_required
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
    

@login_required
def result(request):
    if 'points' not in request.session:
        return redirect('Quiz:quiz')

    points = request.session['points']
    del request.session['points']

    new_entry = LeaderboardEntry(user_name=request.user, score=points)
    new_entry.save()

    leaderboard = LeaderboardEntry.objects.all()[:10]

    return render(request, 'Quiz/result.html', {'points': points, 'leaderboard': leaderboard})





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Quiz:quiz')
    else:
        form = RegistrationForm()
    return render(request, 'Quiz/register.html', {'form': form})


@login_required
def quiz_config(request):
    if request.method == 'POST':
        form = QuizConfigForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data['category']
            difficulty = form.cleaned_data['difficulty']
            question_type = form.cleaned_data['question_type']

            request.session['quiz_config'] = {
                'category': category,
                'difficulty': difficulty,
                'question_type': question_type,
            }
            return redirect('Quiz:quiz')
    else:
        form = QuizConfigForm()

    return render(request, 'Quiz/quiz_config.html', {'form': form})