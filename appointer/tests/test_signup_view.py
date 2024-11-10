from datetime import timedelta

from django.urls import reverse
from django.utils import timezone

from django.test import TestCase

from appointer.models import Event, Signup


class SignupTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            name="Event",
            start_timestamp=timezone.now() + timedelta(days=1),
            end_timestamp=timezone.now() + timedelta(days=2)
        )


    def test_should_signup_to_event_with_name_and_redirect_to_event_detail_view(self):
        """
        Test that the signup form correctly creates a Signup instance and redirects.
        """
        response = self.client.post(reverse("appointer:signup", args=[self.event.id]), data={"new_signup": "Test User"})

        self.assertEqual(Signup.objects.count(), 1)
        signup_instance = Signup.objects.first()
        self.assertEqual(signup_instance.name, "Test User")
        self.assertEqual(signup_instance.event, self.event)
        self.assertRedirects(response, reverse("appointer:event_detail", args=[self.event.id]))


    def test_signup_event_not_found(self):
        """
        Test that trying to signup for a non-existent event raises a 404 error.
        """
        non_existent_event_id = 9999
        response = self.client.post(reverse("appointer:signup", args=[non_existent_event_id]), data={
            "new_signup": "Test User"
        })
        self.assertEqual(response.status_code, 404)


    def test_signup_missing_name(self):
        """
        Test that an empty 'new_signup' field doesn't create a Signup instance.
        """
        post_data = {
            "new_signup": ""
        }
        response = self.client.post(reverse("appointer:signup", args=[self.event.id]), data=post_data)

        self.assertEqual(Signup.objects.count(), 0)
        self.assertEqual(response.status_code, 400)