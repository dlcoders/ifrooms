from django.forms import ModelForm
from django import forms
from .models import Reservation


class CreateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "date",
            "startTime",
            "endTime",
            "justification",
            "periodicity",
            "annex",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control","data-date-format": "dd/mm/yyyy" }),
            "startTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "endTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "justification": forms.Select(attrs={"class": "form-control"}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
        }

class UpdateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "date",
            "startTime",
            "endTime",
            "justification",
            "periodicity",
            "annex",
            "message",
            "reply",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "data-date-format": "dd/mm/yyyy" }),
            "startTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "endTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "justification": forms.Select(attrs={"class": "form-control"}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
            "message": forms.TextInput(attrs={"class": "form-control", "disabled": "disabled"}),
            "reply": forms.TextInput(attrs={"class": "form-control"}),
        }
        
        def __init__(self, *args, **kwargs):
            super(UpdateReservationForm, self).__init__(*args, **kwargs)
            # Set the initial value for the date field
            if self.instance and self.instance.date:
                self.fields['date'].initial = self.instance.date.strftime('%Y-%m-%d')

class CoordinatorGrantsReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "date",
            "startTime",
            "endTime",
            "justification",
            "periodicity",
            "annex",
            "message",
            "reply",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control",'data-date-format': 'dd/mm/yyyy' }),
            "startTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "endTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "justification": forms.Select(attrs={"class": "form-control"}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
            "message": forms.TextInput(attrs={"class": "form-control"}),
            "reply": forms.TextInput(
                attrs={"class": "form-control", "disabled": "disabled"}
            ),
        }
