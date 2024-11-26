from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Event, Signup

class IndexView(generic.ListView):
    template_name = "appointer/index.html"
    context_object_name = "upcoming_events_list"

    def get_queryset(self):
        now = timezone.now()
        return Event.objects.filter(end_timestamp__gte=now).order_by("start_timestamp")[:5]


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "appointer/event_detail.html"


def signup(request: HttpRequest, event_id: int):
    event = get_object_or_404(Event, pk=event_id)
    name_in_form = request.POST["new_signup"]
    if not name_in_form.strip():
        return HttpResponseBadRequest(reason="No name provided")
    else:
        signup_instance = Signup(event=event, name=name_in_form)
        signup_instance.save()
        return HttpResponseRedirect(reverse("appointer:event_detail", args=(event.id,)))


def signout(request: HttpRequest, event_id: int, signout_id: int):
    event = get_object_or_404(Event, pk=event_id)

    signup_instance = Signup.objects.get(id=signout_id)
    signup_instance.delete()
    return HttpResponseRedirect(reverse("appointer:event_detail", args=(event.id,)))


def add_event(request: HttpRequest):
    if request.method == 'POST':
        print(request.POST["event_start_timestamp"])
        start_timestamp = request.POST["event_start_timestamp"] # TODO Make timezone aware
        end_timestamp = request.POST["event_end_timestamp"] # TODO Make timezone aware
        event_instance = Event.objects.create(
            name=request.POST["event_name"],
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp
        )
        event_instance.save()
        return HttpResponseRedirect(reverse("appointer:event_detail", args=(event_instance.pk,)))
    else:
        return render(request, "appointer/add_event.html")
