from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from game.engine import generate_data
from accounts.models import GameUser
from .models import SingleplayerGame, MultiplayerGame
from .forms import SingleplayerGameForm
import pandas as pd
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go
import django.utils.timezone as tz
import datetime
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

        dataframe = generate_data.generate_data(difficulty=form.data["difficulty"])

        form.data['Start'] = dataframe.index[0]
        form.data['End'] = dataframe.index[-1]
        form.data['Data'] = {'data':np.array2string(dataframe["Values"].to_numpy())}
        form.data['Predictions'] = {'data':np.array2string(dataframe["Predictions"].to_numpy())}

        if form.is_valid():
            model = form.save()
        else:
            print(form.errors)
        
        return redirect('/game/singleplayer/' + str(model.pk))
    else:
        form = SingleplayerGameForm()

    return render(request, "game/create_single_player_game.html", {'form': form})

@login_required(login_url='/accounts/login/')
def SinglePlayerGameView(request, game_id):
    game = SingleplayerGame.objects.get(game_id=game_id)

    game_data = np.fromstring(game.Data['data'][1:-1], dtype=int, sep=' ')
    prediction_data = np.fromstring(game.Predictions['data'][1:-1], dtype=int, sep=' ')
    start_date = game.Start.date()
    end_date = game.End.date()
    date_array = pd.date_range(start=start_date,end=end_date, freq=datetime.timedelta(days=1))

    figure = go.FigureWidget()
    config = {'displaylogo': False}
    figure.update_layout(modebar={
            'orientation': 'v'}, 
        template="plotly_white")
    
    figure.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis = dict(
        tickmode = 'array',
        tickvals =  date_array[::7])
    )
        

    figure.add_trace(go.Scatter(x=date_array, y=game_data, name="Values", mode='lines'))
    plt = plot(figure, output_type="div", config=config)

    return render(request, 'game/single_player_game.html', {'game_id':game_id, 'game':game, 'plot_div':plt})

