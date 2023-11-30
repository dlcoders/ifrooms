from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.calendarapp.views.other_views import CalendarViewNew

from apps.rooms.models import Room
from django.views.generic import ListView


# Form Deferir Reserva
class CoordinatorGrantReservationFormView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = "pages/coordinator/forms/form_grant_reservation.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context


# Deferir Reserva
class GrantsView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = "pages/coordinator/grants.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context


# Reservar Salas
# class TeacherBookingRoomView(LoginRequiredMixin, TemplateView):
#     login_url = "accounts:signin"
#     template_name = "pages/teacher/booking_rooms.html"
    
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['sua_variavel'] = 'Valor do contexto'
#     #     context['outra_variavel'] = 'Outro valor do contexto'
#     #     return context


# Form Fazer Reserva
class TeacherMakeReservationFormView(CalendarViewNew, LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = "pages/teacher/forms/form_make_reservation.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context


# Minhas Reservas
class TeacherReservationFormView(LoginRequiredMixin, TemplateView):
    login_url = "accounts:signin"
    template_name = "pages/teacher/forms/form_reservation.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context


class TeacherMyReservationView(TemplateView):
    template_name = "pages/teacher/my_reservations.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sua_variavel'] = 'Valor do contexto'
    #     context['outra_variavel'] = 'Outro valor do contexto'
    #     return context

# Reservar Salas
class TeacherRoomsListView(ListView):
    model = Room
    template_name = 'pages/teacher/booking_rooms.html'
    context_object_name = 'rooms'  # Nome da variável a ser usada no template
    # paginate_by = 2