from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_confirmation_email(client_email_address):
    try:
        # send_mail(
        #     subject="Reservation Confirmed",
        #     message=f"Dear customer, your reservation has been confirmed.",
        #     from_email='admin@email.com',
        #     recipient_list=[client_email_address],
        #     fail_silently=False)    
        print(f"Email sended succefully to {client_email_address}")
    except Exception as e:
        print(e)