from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.calendarapp.views.other_views import CalendarViewNew
from apps.reservation.form import (
    CoordinatorGrantsReservationForm,
    CreateReservationForm,
    UpdateReservationForm,
)
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
    template_name = "pages/teacher/booking_rooms.html"
    context_object_name = "rooms"  # Nome da variável a ser usada no template
    # paginate_by = 2


class ReservationListView(ListView):
    model = Reservation
    template_name = "reservations/reservations.html"
    context_object_name = "reservations"


class TeacherReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "reservations/my_reservations.html"
    context_object_name = "reservations"

    def get_queryset(self):
        return Reservation.objects.filter(id_user_teacher=self.request.user)


class ReservationCreateView(CreateView):
    template_name = "reservations/form.html"
    form_class = CreateReservationForm
    success_url = reverse_lazy("dashboard")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room_id = self.kwargs.get(self.pk_url_kwarg)
        room = get_object_or_404(Room, id=room_id)
        context["room"] = room
        return context

    def form_valid(self, form):
        room = self.get_context_data().get("room")
        form.instance.id_room = room
        form.instance.id_user_teacher = self.request.user
        form.instance.status = "Aguardando Resposta"
        return super().form_valid(form)


class CoordinatorGrantsReservationView(UpdateView):
    model = Reservation
    form_class = CoordinatorGrantsReservationForm
    template_name = "reservations/form_feedback.html"
    pk_url_kwarg = "id"

    def form_valid(self, form):
        message = form.cleaned_data.get("message")

        if "deferir" in self.request.POST:
            form.instance.status = "Deferido"
        elif "indeferir" in self.request.POST:
            form.instance.status = "Indeferido"
        elif "enviar_feedback" in self.request.POST:
            form.instance.message = message
            form.instance.status = "Aguardando Resposta"

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("reservation:reservation-list")


class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = UpdateReservationForm
    template_name = "reservations/form_feedback.html"
    pk_url_kwarg = "id"

    def get_success_url(self):
        return reverse_lazy("reservation:teacher-reservation-list")


class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy("reservation:reservation-list")
    pk_url_kwarg = "id"
