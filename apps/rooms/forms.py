from django.forms import ModelForm
from django import forms
from .models import Room

class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_name' : forms.TextInput(attrs={'class': 'form-control' }),
            'key' : forms.TextInput(attrs={'class': 'form-control' }),
            'department' : forms.Select(attrs={'class': 'form-control' }),
            'available': forms.Select(attrs={'class': 'form-control' }),
            'id_user_coordinator': forms.Select(attrs={'class': 'form-control' })
        }