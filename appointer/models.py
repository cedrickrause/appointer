from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.name} @ {self.start_timestamp}"


class Signup(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} for {self.event.name}"
