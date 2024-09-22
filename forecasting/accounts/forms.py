from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import GameUser

class GameUserCreationForm(UserCreationForm):
    class Meta:
        model = GameUser
        fields = ("username", "email")

class GameUserChangeForm(UserChangeForm):

    class Meta:
        model = GameUser
        fields = ("username", "email")