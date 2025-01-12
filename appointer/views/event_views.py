from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from appointer.models import Event


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "appointer/event_detail.html"


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


def delete_event(request: HttpRequest, event_id: int):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse("appointer:index"))
