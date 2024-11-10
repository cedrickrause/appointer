from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from django.test import TestCase

from appointer.models import Event


class IndexViewTests(TestCase):
    def test_should_not_display_past_events(self):
        Event.objects.create(
            name="Past Event",
            start_timestamp=timezone.now() - timedelta(days=2),
            end_timestamp=timezone.now() - timedelta(days=1)
        )

        response = self.client.get(reverse("appointer:index"))
        self.assertQuerySetEqual(
            response.context["upcoming_events_list"],
            [],
        )

    def test_should_display_ongoing_events(self):
        ongoing_event = Event.objects.create(
            name="Ongoing Event",
            start_timestamp=timezone.now() - timedelta(days=1),
            end_timestamp=timezone.now() + timedelta(days=1)
        )

        response = self.client.get(reverse("appointer:index"))
        self.assertQuerySetEqual(
            response.context["upcoming_events_list"],
            [ongoing_event],
        )

    def test_should_display_future_events(self):
        future_event = Event.objects.create(
            name="Future Event",
            start_timestamp=timezone.now() + timedelta(days=1),
            end_timestamp=timezone.now() + timedelta(days=2)
        )

        response = self.client.get(reverse("appointer:index"))
        self.assertQuerySetEqual(
            response.context["upcoming_events_list"],
            [future_event],
        )

    def test_should_display_only_five_results(self):
        for index in range(0,5):
            Event.objects.create(
                name="Event " + str(index),
                start_timestamp=timezone.now() + timedelta(days=1),
                end_timestamp=timezone.now() + timedelta(days=2)
            )
        events_list = self.client.get(reverse("appointer:index")).context["upcoming_events_list"]
        self.assertEqual(len(events_list), 5)

