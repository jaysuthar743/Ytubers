from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ContactTeam(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    details_message = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, related_name = 'user', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name