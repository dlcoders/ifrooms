from django.forms import ModelForm, DateInput
from apps.calendarapp.models import Event, EventMember
from django import forms


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "date", "start_time", "end_time",]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o título da aula"}
            ),
            "date": forms.DateInput(
                attrs={"class": "form-control", "data-date-format": "dd/mm/yyyy"}
            ),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "end_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
        }


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]
