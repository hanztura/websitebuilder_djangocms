from django.db import models

from django_extensions.db.models import ActivatorModel, TimeStampedModel


class ContactUs(TimeStampedModel, models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField()
    message = models.TextField()
    other_fields = models.CharField(max_length=1000, blank=True)
    sent = models.BooleanField(default=False, blank=True)
    captcha_verify_response = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        name = '{}: {}'.format(self.name, self.message)
        return name


class Subscriber(TimeStampedModel, ActivatorModel):
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.email_address
