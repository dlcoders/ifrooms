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


class AllEventsListView(ListView):
    """All event list views"""

    template_name = "pages/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_all_events_by_user(user=self.request.user)


class RunningEventsListView(ListView):
    """Running events list view"""

    template_name = "pages/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events_by_user(user=self.request.user)


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = "month=" + str(prev_month.year) + "-" + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month


class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = "accounts:signin"
    model = Event
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_cal)
        context["prev_month"] = prev_month(d)
        context["next_month"] = next_month(d)
        return context


@login_required(login_url="signup")
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]
        description = form.cleaned_data["description"]
        start = form.cleaned_data["start"]
        end = form.cleaned_data["end"]
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start=start,
            end=end,
        )
        return HttpResponseRedirect(reverse("calendarapp:calendar"))
    return render(request, "event.html", {"form": form})


class EventEdit(generic.UpdateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "event.html"


@login_required(login_url="signup")
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {"event": event}
    return render(request, "event-details.html", context)


# view padrão para calendário
# class CalendarViewNew(LoginRequiredMixin, generic.View):
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

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("calendarapp:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        event.delete()
        return JsonResponse({"message": "Evento apagado com sucesso."})
    else:
        return JsonResponse({"message": "Error!"}, status=400)


def next_week(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        next = event
        next.id = None
        next.start_time += timedelta(days=7)
        next.end_time += timedelta(days=7)
        next.save()
        return JsonResponse({"message": "Sucesso!"})
    else:
        return JsonResponse({"message": "Error!"}, status=400)


def next_day(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        next = event
        next.id = None
        next.start_time += timedelta(days=1)
        next.end_time += timedelta(days=1)
        next.save()
        return JsonResponse({"message": "Sucesso!"})
    else:
        return JsonResponse({"message": "Error!"}, status=400)


class MyCalendarStudent(CalendarViewNew):
    template_name = "calendars/student_calendar.html"


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
