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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filtered_reservations = Reservation.objects.filter(
            id_room__id_user_coordinator=self.request.user
        )

        context["reservations"] = filtered_reservations

        return context


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
                    class_school=form.instance.class_school,
                    periodicity=form.instance.periodicity,
                    annex=form.instance.annex,
                    message=form.instance.message,
                    reply=form.instance.reply,
                    status=form.instance.status,
                    id_room=form.instance.id_room,
                    id_user_teacher=form.instance.id_user_teacher,
                )

                new_reservation.save()

        form.save()

        return super().form_valid(form)

    def calculate_new_date(self, base_date, periodicity, increment):
        if periodicity == "daily":
            return base_date + timezone.timedelta(days=increment)
        elif periodicity == "weekly":
            return base_date + timezone.timedelta(weeks=increment)
        elif periodicity == "monthly":
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
