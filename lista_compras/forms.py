from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'quantidade','comprado'] # Quais campos queremos que o usuário preencha