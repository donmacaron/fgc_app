from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    # game_title = forms.CharField(initial='Booty Huntress IV')
    # game_description = forms.CharField(initial='Huntress hunts for the booty')

    class Meta:
        model = Game
        fields = ('game_title', 'game_description', 'cover')
        labels = {
            'game_title': 'Название игры',
            'game_description': 'Описание игры',
            'cover': 'Обложка (не обязательно)'
        }
