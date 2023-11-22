from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.accounts.forms import SignInForm

from django.contrib.auth import logout

from apps.accounts.forms import SignUpForm

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class UsersView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = 'pages/admin/users.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    

class SignUpView(View):
    """ User registration view """

    template_name = "accounts/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("accounts:signin")
        context = {"form": forms}
        return render(request, self.template_name, context)


def signout(request):
    logout(request)
    return redirect("accounts:signin")


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



class CreateUserView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = 'pages/admin/forms/form_create_user.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
