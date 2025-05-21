from django.core.mail import send_mail
from django.dispatch import Signal, receiver

order_completed = Signal()
