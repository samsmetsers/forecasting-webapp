from django.db import models
from accounts.models import GameUser
import uuid
import django.utils.timezone as tz

EASY = "Easy"
NORMAL = "Normal"
HARD = "Hard"

DIFFICULTY_CHOICES = ((EASY, "Easy"), (NORMAL, "Normal"), (HARD, "Hard"))

# Create your models here.
class Game(models.Model):
    game_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_host = models.ForeignKey(GameUser, name='GameUser', on_delete=models.CASCADE)
    active = models.BooleanField(name="Active")
    difficulty = models.CharField(name="difficulty", max_length=6, choices=DIFFICULTY_CHOICES, default="Normal")

    class Meta:
        abstract = True

class SingleplayerGame(Game):
    score = models.FloatField(name="Score")
    start_date = models.DateTimeField(name="Start", db_index=True, default=tz.now)
    end_date = models.DateTimeField(name="End", db_index=True, default=tz.now)
    game_data = models.JSONField(name="Data", default=dict)
    game_predictions = models.JSONField(name="Predictions", default=dict)

class MultiplayerGame(Game):
    players = models.ManyToManyField(GameUser, related_name="Players")