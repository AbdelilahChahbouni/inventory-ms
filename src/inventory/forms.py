from .models import *
from django import forms

class InventoryStockForm(forms.ModelForm):
    class Meta:
        model = InventoryStock
        fields = ['name' , 'quantity']

