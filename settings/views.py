from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from apps.calendarapp.models import Event


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "pages/dashboard.html"

    def get(self, request, *args, **kwargs):
        # events = Event.objects.get_all_events_by_user(user=request.user)
        # running_events = Event.objects.get_running_events_by_user(user=request.user)
        # latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        # context = {
        #     "total_event": events.count(),
        #     "running_events": running_events,
        #     "latest_events": latest_events,
        # }
        # return render(request, self.template_name, context)
        return render(request, self.template_name)
