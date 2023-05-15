from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Quiz.models import LeaderboardEntry
from Quiz.forms import QuizConfigForm, RegistrationForm

class QuizViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

    def test_quiz_config_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("Quiz:quiz_config"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], QuizConfigForm)

    

    def test_register_view_get(self):
        response = self.client.get(reverse("Quiz:register"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], RegistrationForm)

    def test_register_view_post(self):
        response = self.client.post(reverse("Quiz:register"), {
            "username": "newuser",
            "password1": "testowy1910",
            "password2": "testowy1910"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view_get(self):
        response = self.client.get(reverse("Quiz:login"))
        self.assertEqual(response.status_code, 200)

    def test_login_view_post(self):
        response = self.client.post(reverse("Quiz:login"), {
            "username": "testuser",
            "password": "testpassword"
        })
        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("Quiz:logout"))
        self.assertEqual(response.status_code, 302)
