from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.calendarapp.views.other_views import CalendarViewNew
from apps.reservation.form import ReservationForm
from apps.reservation.models import Reservation

from apps.rooms.models import Room
from django.views.generic import ListView

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

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

    
class ReservationListView(ListView):
    model = Reservation
    template_name = "reservations/reservations.html"
    context_object_name = "reservations"  # Nome da variável a ser usada no template
    # paginate_by = 10


class ReservationCreateView(CreateView):
    template_name = "reservations/form.html"
    form_class = ReservationForm
    success_url = reverse_lazy("room:room-list")


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "reservations/form.html"
    pk_url_kwarg = "id"  # Nome da variável na URL

    def get_success_url(self):
        return reverse_lazy("room:room-list")


class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy("room:room-list")
    pk_url_kwarg = "id"

