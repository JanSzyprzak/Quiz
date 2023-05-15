from django.test import TestCase
from django.contrib.auth.models import User
from Quiz.forms import RegistrationForm, QuizConfigForm

class FormsTest(TestCase):

    def test_registration_form(self):
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword"
        }
        form = RegistrationForm(data=form_data)

        self.assertTrue(form.is_valid())
        user = form.save()

        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpassword"))

    def test_quiz_config_form(self):
        form_data = {
            "category": "9",
            "difficulty": "easy",
            "question_type": "multiple"
        }
        form = QuizConfigForm(data=form_data)

        self.assertTrue(form.is_valid())
        cleaned_data = form.cleaned_data

        self.assertEqual(cleaned_data["category"], "9")
        self.assertEqual(cleaned_data["difficulty"], "easy")
        self.assertEqual(cleaned_data["question_type"], "multiple")
