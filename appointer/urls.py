from django.urls import path

from . import views

app_name = "appointer"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),
    path("<int:event_id>/signup/", views.signup, name="signup"),
    path("<int:event_id>/signout/<int:signout_id>", views.signout, name="signout"),
    path("add/", views.add_event, name="add_event"),
    path("<int:event_id>/delete_event/", views.delete_event, name="delete_event"),
]
