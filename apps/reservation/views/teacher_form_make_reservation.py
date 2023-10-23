
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Form Fazer Reserva
class TeacherMakeReservationFormView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = 'pages/teacher/forms/form_make_reservation.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context
    