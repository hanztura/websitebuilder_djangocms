import requests

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.forms import ModelForm, BooleanField, CharField, ValidationError

from .models import ContactUs, Subscriber
from .utils import verify_captcha


class ContactUsForm(ModelForm):
    captcha = CharField()

    class Meta:
        model = ContactUs
        fields = [
            'name',
            'email_address',
            'message',
            'other_fields',
            'sent',
            'captcha_verify_response',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['captcha'].required = True

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        response_content = verify_captcha(captcha)
        if response_content['success']:
            self.cleaned_data['captcha_verify_response'] = response_content
            return captcha
        else:
            msg = 'Unable to verify if you are not a robot.'
            raise ValidationError(msg)

    def send_mail(self):
        host = Site.objects.get_current()
        contact_us = self.cleaned_data
        name = contact_us['name']
        email = contact_us['email_address']
        message = contact_us['message']
        subject = 'Contact Us submitted from: {}'.format(host.domain)
        recepient_list = (
            'hctura.official@gmail.com',
        )

        content_name = 'Name: ' + name
        content_email = 'Email: ' + email
        content_message = 'Message: ' + message
        content = "{}'\n'{}'\n'{}".format(
            content_name, content_email, content_message)

        mail = send_mail(
            subject,
            content,
            email,
            recepient_list
        )
        if mail > 0:
            self.instance.sent = True
            self.instance.save()

        return self.instance

    def verify_captcha(self, captcha):
        verify_url = 'https://www.google.com/recaptcha/api/siteverify'
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': captcha,
        }

        response = requests.post(
            verify_url,
            params=data)
        response_content = response.json()

        return response_content


class SubscriberForm(ModelForm):
    duplicate = BooleanField()

    class Meta:
        model = Subscriber
        fields = ['email_address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duplicate'].required = False
        self.fields['duplicate'].initial = False

    def clean_email_address(self):
        email_address = self.cleaned_data['email_address']
        if Subscriber.objects.filter(email_address=email_address).exists():
            self.add_error('duplicate', True)

        return email_address
