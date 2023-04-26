from django.test import TestCase
from Quiz.models import Category, Question, Quiz, User, Leaderboard


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Geography")

    def test_category_name(self):
        self.assertEqual(str(self.category), "Geography")


class QuestionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Geography")
        self.question = Question.objects.create(text="What is the capital of Poland?", answer="Warsaw", category=self.category, points=1)

    def test_question_text(self):
        self.assertEqual(self.question.text, "What is the capital of Poland?")

    def test_question_answer(self):
        self.assertEqual(self.question.answer, "Warsaw")

    def test_question_category(self):
        self.assertEqual(str(self.question.category), "Geography")

    def test_question_points(self):
        self.assertEqual(self.question.points, 1)


class QuizModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Geography")
        self.user = User.objects.create(name="andrzej", email="andrzej@example.pl", password="password")
        self.quiz = Quiz.objects.create(category=self.category, difficulty="easy", result=5, completed=False)

        self.question_1 = Question.objects.create(text="What is the capital of Poland?", answer="Warsaw", category=self.category, points=1)
        self.question_2 = Question.objects.create(text="What is the capital of Germany?", answer="Berlin", category=self.category, points=1)

    def test_quiz_category(self):
        self.assertEqual(str(self.quiz.category), "Geography")

    def test_quiz_difficulty(self):
        self.assertEqual(self.quiz.difficulty, "easy")

    def test_quiz_result(self):
        self.assertEqual(self.quiz.result, 5)

    def test_quiz_completed(self):
        self.assertFalse(self.quiz.completed)

    def test_quiz_questions(self):
        self.assertEqual(self.quiz.questions.count(), 0)

        # Add a question to the quiz
        self.quiz.questions.add(self.question_1)
        self.assertEqual(self.quiz.questions.count(), 1)

        # Add another question to the quiz
        self.quiz.questions.add(self.question_2)
        self.assertEqual(self.quiz.questions.count(), 2)

        # Remove a question from the quiz
        self.quiz.questions.remove(self.question_1)
        self.assertEqual(self.quiz.questions.count(), 1)


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="andrzej", email="andrzej@example.pl", password="password")

    def test_user_name(self):
        self.assertEqual(self.user.name, "andrzej")

    def test_user_email(self):
        self.assertEqual(self.user.email, "andrzej@example.pl")

    def test_user_password(self):
        self.assertEqual(self.user.password, "password")


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(name="andrzej", email="andrzej@example.pl", password="password")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=10)

    def test_leaderboard_user(self):
        self.assertEqual(str(self.leaderboard.user), "andrzej")

    def test_leaderboard_score(self):
        self.assertEqual(self.leaderboard.score, 10)
