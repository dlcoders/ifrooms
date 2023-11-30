from django.forms import ModelForm
from django import forms
from .models import Reservation

class RoomForm(ModelForm):

    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'date' : forms.DateField(attrs={'class': 'form-control' }),
            'startTime' : forms.DateInput(attrs={'class': 'form-control' }),
            'endTime' : forms.DateInput(attrs={'class': 'form-control' }),
            'justification': forms.Select(attrs={'class': 'form-control' }),
            'periodicity': forms.Select(attrs={'class': 'form-control' }),
            'annex': forms.FileInput(attrs={'class': 'form-control' }),
            'message': forms.TextInput(attrs={'class': 'form-control' }),
            'reply': forms.TextInput(attrs={'class': 'form-control' }),
            'status': forms.Select(attrs={'class': 'form-control' }),
            'id_room': forms.Select(attrs={'class': 'form-control' }),
            'id_user_teacher': forms.Select(attrs={'class': 'form-control' }),
            'id_user_coordinator': forms.Select(attrs={'class': 'form-control' }),
        }