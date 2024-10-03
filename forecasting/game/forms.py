from django.forms import ModelForm
from .models import SingleplayerGame, MultiplayerGame

class SingleplayerGameForm(ModelForm):
    class Meta:
        model = SingleplayerGame
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
