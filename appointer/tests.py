from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from django.test import TestCase

from appointer.models import Event


class IndexViewTests(TestCase):
    def test_should_not_display_past_events(self):
        past_event = Event.objects.create(
            name="Past Event",
            start_timestamp=timezone.now() - timedelta(days=2),
            end_timestamp=timezone.now() - timedelta(days=1)
        )
        ongoing_event = Event.objects.create(
            name="Ongoing Event",
            start_timestamp=timezone.now() - timedelta(days=1),
            end_timestamp=timezone.now() + timedelta(days=1)
        )
        future_event = Event.objects.create(
            name="Future Event",
            start_timestamp=timezone.now() + timedelta(days=1),
            end_timestamp=timezone.now() + timedelta(days=2)
        )

        response = self.client.get(reverse("appointer:index"))
        self.assertQuerySetEqual(
            response.context["upcoming_events_list"],
            [ongoing_event, future_event],
        )


