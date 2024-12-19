from django.db import models

from django.db import models
from enum import Enum

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class ReservationStatus(Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    NO_SHOW = "NO_SHOW"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    reservation_date = models.DateField()
    status = models.CharField(max_length=100, choices=ReservationStatus.choices())
