from django.db import models

class LeaderboardEntry(models.Model):
    user_name = models.CharField(max_length=100)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', 'timestamp']

    def __str__(self):
        return f"{self.user_name} - {self.score}"
