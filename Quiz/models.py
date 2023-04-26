from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.category}: {self.text}"


class Quiz(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    result = models.IntegerField()
    completed = models.BooleanField(default=False)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"{self.category} - {self.difficulty} - {self.result}"


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.score}"
