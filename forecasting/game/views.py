from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from game.engine import generate_data
from accounts.models import GameUser
from .models import SingleplayerGame, MultiplayerGame
from .forms import SingleplayerGameForm
import pandas as pd
from plotly.offline import plot
import plotly.express as px
import django.utils.timezone as tz
import pickle

# Create your views here.
@login_required(login_url='/accounts/login/')
def SingleplayerView(request):
    try:
        games = SingleplayerGame.objects.filter(GameUser_id=request.user.id)
        any_active = games.filter(Active=True)
    except:
        games = []

    context = {'games': games, 'any_active':any_active}

    return render(request, 'game/single_player.html', context)

@login_required(login_url='/accounts/login/')
def CreateSinglePlayerGameView(request):
    if request.method == 'POST':
        form = SingleplayerGameForm(request.POST)

        form.data._mutable = True

        form.data['GameUser'] = request.user
        form.data['Score'] = 0.0
        form.data['Active'] = True
        form.data['Start'] = tz.now()
        form.data['End'] = tz.now()

        if form.is_valid():
            model = form.save()
            dataframe = generate_data.generate_data(difficulty=model.difficulty)
            model.start = dataframe.index[0]
            model.end = dataframe.index[-1]
            model.game_data = pickle.dumps(dataframe["Values"].to_numpy())
            model.prediction_data = pickle.dumps(dataframe["Predictions"].to_numpy())
            model.save()
            print(model.end)
        else:
            print(form.errors)
        
        return redirect('/game/singleplayer/' + str(model.pk))
    else:
        form = SingleplayerGameForm()

    return render(request, "game/create_single_player_game.html", {'form': form})

@login_required(login_url='/accounts/login/')
def SinglePlayerGameView(request, game_id):
    game = SingleplayerGame.objects.get(game_id=game_id)
    return render(request, 'game/single_player_game.html', {'game_id':game_id, 'game':game})

