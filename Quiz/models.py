from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.name

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.subject} - {self.difficulty} - {self.points}"
    
class Question(models.Model):
    text = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=20)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} - {self.difficulty} - {self.text}"
