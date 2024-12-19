from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Reservation
from .tasks import send_confirmation_email

@receiver(post_save, sender=Reservation)
def reservation_post_save(sender, instance, created, **kwargs):
    if created:
        send_confirmation_email(instance.client.email)
