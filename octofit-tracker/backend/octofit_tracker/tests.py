from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.assertEqual(str(team), 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC superheroes')
        user = User.objects.create(email='batman@dc.com', username='Batman', team=team, is_superhero=True)
        self.assertEqual(str(user), 'Batman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel2', description='Marvel superheroes')
        user = User.objects.create(email='spiderman@marvel.com', username='Spiderman', team=team, is_superhero=True)
        activity = Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, date='2025-10-26')
        self.assertEqual(str(activity), 'Spiderman - Running')

    def test_workout_creation(self):
        team = Team.objects.create(name='DC2', description='DC superheroes')
        workout = Workout.objects.create(name='Pushups', description='Upper body', suggested_for_team=team)
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Marvel3', description='Marvel superheroes')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(str(leaderboard), 'Marvel3 - 100 pts')
