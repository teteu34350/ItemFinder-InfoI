from django import forms
from .models import ItemPerdido, ItemAchado

class ItemPerdidoForm(forms.ModelForm):
    class Meta:
        model = ItemPerdido
        fields = ['nome', 'desc', 'foto', 'data', 'local', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class ItemAchadoForm(forms.ModelForm):
    class Meta:
        model = ItemAchado
        fields = ['nome', 'desc', 'foto', 'data', 'local', 'categoria']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
