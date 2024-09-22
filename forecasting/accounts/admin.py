from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import GameUserChangeForm, GameUserCreationForm
from .models import GameUser
# Register your models here.

class GameUserAdmin(UserAdmin):
    add_form = GameUserCreationForm
    form = GameUserChangeForm
    model = GameUser
    list_display = ["email", "username"]

admin.site.register(GameUser, GameUserAdmin)