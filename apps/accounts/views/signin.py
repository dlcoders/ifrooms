from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.accounts.forms import SignInForm


class SignInView(View):
    """ User registration view """

    template_name = "accounts/signin.html"
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            matricula = forms.cleaned_data["matricula"]
            password = forms.cleaned_data["password"]
            user = authenticate(matricula=matricula, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                forms.error_message = "Credenciais inválidas. Verifique sua matrícula e senha."
        context = {"form": forms}
        return render(request, self.template_name, context)

