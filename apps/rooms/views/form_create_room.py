
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateRoomFormView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = 'pages/coordinator/forms/form_create_room.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    