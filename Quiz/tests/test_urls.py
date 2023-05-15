from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.views import LoginView, LogoutView
from Quiz import views

class QuizURLsTest(TestCase):
    
    def test_quiz_url(self):
        url = reverse('Quiz:quiz')
        self.assertEqual(resolve(url).func, views.fetch_data)

    def test_submit_answers_url(self):
        url = reverse('Quiz:submit_answers')
        self.assertEqual(resolve(url).func, views.submit_answers)

    def test_result_url(self):
        url = reverse('Quiz:result')
        self.assertEqual(resolve(url).func, views.result)

    def test_login_url(self):
        url = reverse('Quiz:login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout_url(self):
        url = reverse('Quiz:logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_register_url(self):
        url = reverse('Quiz:register')
        self.assertEqual(resolve(url).func, views.register)

    def test_quiz_config_url(self):
        url = reverse('Quiz:quiz_config')
        self.assertEqual(resolve(url).func, views.quiz_config)
