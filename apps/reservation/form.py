from django.forms import ModelForm
from django import forms
from .models import Reservation


from django.forms import ModelForm
from django import forms
from .models import Reservation


class CreateReservationForm(ModelForm):
    num_occurrences = forms.IntegerField(
        label="Número de ocorrências",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Reservation
        fields = [
            "date",
            "start_time",
            "end_time",
            "justification",
            "class_school",
            "periodicity",
            "annex",
            "num_occurrences",
        ]
        widgets = {
            "date": forms.DateInput(
                attrs={"class": "form-control", "type":"date", "data-date-format": "dd/mm/yyyy"}
            ),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "end_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "class_school": forms.TextInput(attrs={"class": "form-control"}),
            "justification": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
        }


class UpdateReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "date",
            "start_time",
            "end_time",
            "class_school",
            "justification",
            "periodicity",
            "annex",
            "message",
            "reply",
        ]
        widgets = {
            "date": forms.DateInput(
                attrs={"class": "form-control", "data-date-format": "dd/mm/yyyy"}
            ),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "end_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "justification": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "class_school": forms.TextInput(attrs={"class": "form-control"}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
            "message": forms.TextInput(
                attrs={"class": "form-control", "disabled": "disabled"}
            ),
            "reply": forms.TextInput(attrs={"class": "form-control"}),
        }

        def __init__(self, *args, **kwargs):
            super(UpdateReservationForm, self).__init__(*args, **kwargs)
            # Set the initial value for the date field
            if self.instance and self.instance.date:
                self.fields["date"].initial = self.instance.date.strftime("%Y-%m-%d")


class CoordinatorGrantsReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "date",
            "start_time",
            "end_time",
            "class_school",
            "justification",
            "periodicity",
            "annex",
            "message",
            "reply",
        ]
        widgets = {
            "date": forms.DateInput(
                attrs={"class": "form-control", "data-date-format": "dd/mm/yyyy"}
            ),
            "start_time": forms.TimeInput(
                attrs={"class": "form-control", "type": "time"}
            ),
            "end_time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "justification": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "class_school": forms.TextInput(attrs={"class": "form-control"}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
            "message": forms.TextInput(attrs={"class": "form-control"}),
            "reply": forms.TextInput(
                attrs={"class": "form-control", "disabled": "disabled"}
            ),
        }
