from django.contrib import admin
from .models import MultiplayerGame, SingleplayerGame
# Register your models here.
# admin.site.register(GameChart)
admin.site.register(MultiplayerGame)
admin.site.register(SingleplayerGame)