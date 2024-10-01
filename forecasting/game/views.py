from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GameChart, SingleplayerGame, MultiplayerGame
import pandas as pd
from plotly.offline import plot
import plotly.express as px

# Create your views here.
@login_required(login_url='/accounts/login/')
def SingleplayerView(request):
    context = {'plot_div': 'working context!!'}
    return render(request, 'game/single_player.html', context)