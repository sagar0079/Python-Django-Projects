# type: ignore
from django import forms
from .models import FoodList

class AddItemForm(forms.ModelForm):
    class Meta:
        model = FoodList
        fields = '__all__'