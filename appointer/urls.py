from django.urls import path

from .views import views, signup_views, event_views

app_name = "appointer"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", event_views.EventDetailView.as_view(), name="event_detail"),
    path("<int:event_id>/signup/", signup_views.signup, name="signup"),
    path("<int:event_id>/signout/<int:signout_id>", signup_views.signout, name="signout"),
    path("add/", event_views.add_event, name="add_event"),
    path("<int:event_id>/delete_event/", event_views.delete_event, name="delete_event"),
]
