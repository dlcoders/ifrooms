from datetime import datetime
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from dateutil.relativedelta import relativedelta

from apps.reservation.form import (
    CoordinatorGrantsReservationForm,
    CreateReservationForm,
    UpdateReservationForm,
)
from apps.reservation.models import Reservation

from apps.rooms.models import Room
from apps.calendarapp.models import Event

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


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

        num_occurrences = form.cleaned_data.get("num_occurrences", 1)

        if form.instance.periodicity:
            for i in range(1, num_occurrences):
                new_date = self.calculate_new_date(
                    form.instance.date, form.instance.periodicity, i
                )
                new_reservation = Reservation(
                    date=new_date,
                    startTime=form.instance.startTime,
                    endTime=form.instance.endTime,
                    justification=form.instance.justification,
                    periodicity=form.instance.periodicity,
                    annex=form.instance.annex,
                    message=form.instance.message,
                    reply=form.instance.reply,
                    status=form.instance.status,
                    id_room=form.instance.id_room,
                    id_user_teacher=form.instance.id_user_teacher,
                )

                Event.objects.get_or_create(
                    user=self.request.user,
                    title=form.instance.get_justification_display,
                    start=datetime.combine(form.instance.date, form.instance.startTime),
                    end=datetime.combine(form.instance.date, form.instance.endTime),
                )

                new_reservation.save()

        Event.objects.get_or_create(
            user=self.request.user,
            title=form.instance.get_justification_display,
            start=datetime.combine(form.instance.date, form.instance.startTime),
            end=datetime.combine(form.instance.date, form.instance.endTime),
        )

        form.save()

        return super().form_valid(form)

    def calculate_new_date(self, base_date, periodicity, increment):
        if periodicity == "Diária":
            return base_date + timezone.timedelta(days=increment)
        elif periodicity == "Semanal":
            return base_date + timezone.timedelta(weeks=increment)
        elif periodicity == "Mensal":
            return base_date + relativedelta(months=increment)


class CoordinatorGrantsReservationView(UpdateView):
    model = Reservation
    form_class = CoordinatorGrantsReservationForm
    template_name = "reservations/form_grants.html"
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
    success_url = reverse_lazy("reservation:reservation-list")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.render_to_response(
            self.get_context_data(form=form, reservation=self.object)
        )


class ReservationDeleteView(DeleteView):
    model = Reservation
    success_url = reverse_lazy("reservation:reservation-list")
    pk_url_kwarg = "id"
