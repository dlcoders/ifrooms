from django.forms import ModelForm
from django import forms
from .models import Reservation


from django.forms import ModelForm
from django import forms
from .models import Reservation

class CreateReservationForm(ModelForm):
    num_occurrences = forms.IntegerField(
        label="Number of Occurrences",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        required=False,
    )

    class Meta:
        model = Reservation
        fields = [
            "date",
            "startTime",
            "endTime",
            "justification",
            "periodicity",
            "annex",
            "num_occurrences",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "data-date-format": "dd/mm/yyyy"}),
            "startTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "endTime": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "justification": forms.Select(attrs={"class": "form-control"}),
            "periodicity": forms.Select(attrs={"class": "form-control"}),
            "annex": forms.FileInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        # Retrieve the value of the num_occurrences field
        num_occurrences = self.cleaned_data.get("num_occurrences", 1)

        # Call the save method on the model instance and pass num_occurrences
        instance = super().save(commit=False)
        instance.save(num_occurrences=num_occurrences)

        return instance

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
