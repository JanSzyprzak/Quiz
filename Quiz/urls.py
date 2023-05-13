from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Quiz'

urlpatterns = [
    path('quiz', views.fetch_data, name='quiz'), 
    path('submit/', views.submit_answers, name='submit_answers'),
    path('result/', views.result, name='result'),
    path('login/', auth_views.LoginView.as_view(template_name='Quiz/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.quiz_config, name='quiz_config'),
]


    