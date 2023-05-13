from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class QuizConfigForm(forms.Form):
    CATEGORY_CHOICES = [
        ('9', 'General Knowledge'),
        ('10', 'Entertainment: Books'),
        ('11', 'Entertainment: Film'),
        ('12', 'Entertainment: Music'),
        ('13', 'Entertainment: Musicals & Theatres'),
        ('14', 'Entertainment: Television'),
        ('15', 'Entertainment: Video Games'),
        ('16', 'Entertainment: Board Games'),
        ('17', 'Science & Nature'),
        ('18', 'Science: Computers'),
        ('19', 'Science: Mathematics'),
        ('20', 'Mythology'),
        ('21', 'Sports'),
        ('22', 'Geography'),
        ('23', 'History'),
        ('24', 'Politics'),
        ('25', 'Art'),
        ('26', 'Celebrities'),
        ('27', 'Animals'),
        ('28', 'Vehicles'),
        ('29', 'Entertainment: Comics'),
        ('30', 'Science: Gadgets'),
        ('31', 'Entertainment: Japanese Anime & Manga'),
        ('32', 'Entertainment: Cartoon & Animations'),
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    TYPE_CHOICES = [
        ('multiple', 'Multiple Choice'),
        ('boolean', 'True/False'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Category')
    difficulty = forms.ChoiceField(choices=DIFFICULTY_CHOICES, label='Difficulty')
    question_type = forms.ChoiceField(choices=TYPE_CHOICES, label='Type')
