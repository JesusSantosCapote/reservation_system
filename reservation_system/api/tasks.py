from celery import shared_task

@shared_task
def send_confirmation_email(client_email_address):
    """dummy send email function as example"""
    print(f"Email sended to {client_email_address}")