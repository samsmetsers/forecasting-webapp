from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import GameUser
from .models import GameChart, SingleplayerGame, MultiplayerGame
from .forms import SingleplayerGameForm
import pandas as pd
from plotly.offline import plot
import plotly.express as px

# Create your views here.
@login_required(login_url='/accounts/login/')
def SingleplayerView(request):
    try:
        games = SingleplayerGame.objects.filter(GameUser_id=request.user.id)
        any_active = games.filter(Active=True)
    except:
        games = []

    if any_active:
        any_active = True
    else:
        any_active = False

    context = {'games': games, 'any_active':any_active}

    return render(request, 'game/single_player.html', context)

@login_required(login_url='/accounts/login/')
def SinglePlayerGameView(request):
    return render(request, 'game/single_player_game.html', {'nothing':'nothing'})

@login_required(login_url='/accounts/login/')
def CreateSinglePlayerGameView(request):
    if request.method == 'POST':
        form = SingleplayerGameForm(request.POST)

        form.data._mutable = True

        form.data['GameUser'] = request.user
        form.data['Score'] = 0.0
        form.data['Active'] = True

        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        
        return redirect('/game/singleplayer')
    else:
        form = SingleplayerGameForm()

    return render(request, "game/create_single_player_game.html", {'form': form})