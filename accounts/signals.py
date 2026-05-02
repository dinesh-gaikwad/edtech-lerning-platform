from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import UserSession

@receiver(user_logged_in)
def save_user_session_and_send_email(sender, request, user, **kwargs):
    # Save user session
    ip = request.META.get('REMOTE_ADDR')
    UserSession.objects.create(user=user, ip_address=ip)
    
    # Send welcome email
    send_mail(
        subject='Welcome to EdTech Platform!',
        message=f'Hi {user.first_name or user.username},\n\nWelcome to our platform. You logged in successfully from {ip}.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=True,  # Don't crash if email fails
    )