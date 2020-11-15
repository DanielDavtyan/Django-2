from django.forms import ModelForm, TextInput
from .models import ObjectInfo


class CityForm(ModelForm):
    class Meta:
        model = ObjectInfo
        fields = ['cityName']
        widgets = {'cityName': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
