from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from apps.accounts.models import User


class SignInForm(forms.Form):
    matricula = forms.CharField(
        label="Matrícula",
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class SignUpForm(forms.ModelForm):
    matricula = forms.CharField(
        label="Matrícula",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=12,
        required=True,
        help_text="Máximo de 12 caracteres",
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[validate_password],
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        validators=[validate_password],
    )

    class Meta:
        model = User
        fields = ["matricula", "email"]
        widgets = {"email": forms.EmailInput(attrs={"class": "form-control"})}
        
    def clean_matricula(self):
        matricula = self.cleaned_data.get("matricula")
        if len(matricula) > 12:
            raise forms.ValidationError("A matrícula não pode ter mais de 12 caracteres.")
        return matricula

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password didn't match!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
