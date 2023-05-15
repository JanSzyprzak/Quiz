from django.test import TestCase
from Quiz.models import LeaderboardEntry

class LeaderboardEntryModelTest(TestCase):

    def test_leaderboard_entry_creation(self):
        entry = LeaderboardEntry.objects.create(user_name="testuser", score=10)

        self.assertEqual(entry.user_name, "testuser")
        self.assertEqual(entry.score, 10)
        self.assertIsNotNone(entry.timestamp)

    def test_leaderboard_entry_str_representation(self):
        entry = LeaderboardEntry.objects.create(user_name="testuser", score=5)

        self.assertEqual(str(entry), "testuser - 5")

    def test_leaderboard_entry_ordering(self):
        entry1 = LeaderboardEntry.objects.create(user_name="user1", score=10)
        entry2 = LeaderboardEntry.objects.create(user_name="user2", score=15)
        entry3 = LeaderboardEntry.objects.create(user_name="user3", score=5)

        entries = LeaderboardEntry.objects.all()

        self.assertEqual(entries[0], entry2)
        self.assertEqual(entries[1], entry1)
        self.assertEqual(entries[2], entry3)
