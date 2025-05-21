from django.core.mail import send_mail
from django.dispatch import Signal, receiver

order_completed = Signal()


@receiver(order_completed)
def handle_order_completed(sender, order, **kwargs):
    send_mail(
        subject="Your order approved",
        message=f"Thanks for your trust! Your order ID is {order.id}.",
        from_email=None,
        recipient_list=[order.user.email]
    )