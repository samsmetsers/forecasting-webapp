from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/game/singleplayer/(?P<game_id>\w+)/$", consumers.SingleplayerGameConsumer.as_asgi()),
]