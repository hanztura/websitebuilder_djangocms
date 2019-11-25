from django.contrib import admin

from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'email_address',
        'message',
        'other_fields',
        'sent',
        'captcha_verify_response',
        'created',
        'modified',
    ]
    readonly_fields = ['created', 'modified']


admin.site.register(ContactUs, ContactUsAdmin)
