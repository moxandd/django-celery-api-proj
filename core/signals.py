from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Newsletter
import requests

@receiver(post_save, sender=Newsletter)
def trigger_newsletter(sender, instance, created, **kwargs):
    response = requests.get(f"http://127.0.0.1:8000/test/{instance.id}/")
    if response.status_code == 200:
        print("Request compeleted successfully")
    else:
        print(f"Request is not completed, status code: [{response.status_code}]")