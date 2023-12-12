from django.forms import ModelForm, DateInput
from apps.calendarapp.models import Event, EventMember
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "start", "end",]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o título da aula"}
            ),
            "start": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "end": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
        }


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]
