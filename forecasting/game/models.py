from django.db import models
from accounts.models import GameUser

# Create your models here.
class Game(models.Model):
    game_id = models.PositiveBigIntegerField(primary_key=True)
    game_host = models.ForeignKey(GameUser, name='Game host', on_delete=models.CASCADE)
    active = models.BooleanField(name="Active Game")

    class Meta:
        abstract = True

class SingleplayerGame(Game):
    score = models.FloatField(name="Game score")

class MultiplayerGame(Game):
    players = models.ManyToManyField(GameUser, related_name="Players")

class GameChart(models.Model):
    game_id = models.ForeignKey(SingleplayerGame, on_delete=models.CASCADE)