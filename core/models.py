from django.db import models
import uuid

# Create your models here.

class Newsletter(models.Model):
    send_start = models.DateTimeField()
    text_message = models.TextField(max_length=1000, blank=True, null=True)
    mobile_code = models.CharField(max_length=3)
    send_end = models.DateTimeField()

    def __str__(self):
        return f"Newsletter --- {self.id}"
    
class Client(models.Model):
    phone = models.CharField(max_length=11)
    mobile_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=100, blank=True, null=True)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f"Client --- {self.id}"
    
class Message(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    send_status = models.BooleanField(default=False)
    newsletter_id = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    send_to = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message --- {self.id}"