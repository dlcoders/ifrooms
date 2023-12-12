from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from apps.calendarapp.models import Event
from apps.calendarapp.utils import Calendar
from apps.calendarapp.forms import EventForm


class CalendarViewNew(generic.View):
    # login_url = "accounts:signin"
    template_name = "pages/dashboard.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events_by_user(user=request.user)
        events_month = Event.objects.get_running_events_by_user(user=request.user)
        event_list = []

        for event in events:
            if event.status == "Deferido":
                event_list.append(
                    {
                        "id": event.id,
                        "title": event.title,
                        "start": event.start.strftime("%Y-%m-%dT%H:%M:%S"),
                        "end": event.end.strftime("%Y-%m-%dT%H:%M:%S"),
                        "status": event.status,
                    }
                )
        context = {"form": forms, "events": event_list, "events_month": events_month}
        return render(request, self.template_name, context)


class MyCalendarTeacher(CalendarViewNew):
    template_name = "calendars/teacher_calendar.html"


class GeneralCalendar(generic.View):
    template_name = "calendars/general_calendar.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events()
        events_month = Event.objects.get_running_events()
        event_list = []

        for event in events:
            if event.status == "Deferido":
                event_list.append(
                    {
                        "id": event.id,
                        "title": event.title,
                        "start": event.start.strftime("%Y-%m-%dT%H:%M:%S"),
                        "end": event.end.strftime("%Y-%m-%dT%H:%M:%S"),
                        "status": event.status,
                    }
                )
        context = {"form": forms, "events": event_list, "events_month": events_month}
        return render(request, self.template_name, context)
