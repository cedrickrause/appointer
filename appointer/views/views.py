from django.utils import timezone
from django.views import generic

from appointer.models import Event

class IndexView(generic.ListView):
    template_name = "appointer/index.html"
    context_object_name = "upcoming_events_list"

    def get_queryset(self):
        now = timezone.now()
        return Event.objects.filter(end_timestamp__gte=now).order_by("start_timestamp")[:5]
