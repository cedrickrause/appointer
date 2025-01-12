from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse

from appointer.models import Event, Signup


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
