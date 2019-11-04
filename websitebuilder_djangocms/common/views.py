import json

from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic.base import View

from .forms import ContactUsForm


class ContactUsFormView(View):
    http_method_names = ['post']

    # def post(self, request, *args, **kwargs):
    #     referer = request.META['HTTP_REFERER']
    #     form = ContactUsForm(request.POST)
    #     form_sent = False
    #     if form.is_valid():
    #         form.save()
    #         form.send_mail()
    #         try:
    #             del request.session['form']
    #         except Exception as e:
    #             pass
    #     else:
    #         form = {
    #             'name': form.instance.name,
    #             'email_address': form.instance.email_address,
    #             'message': form.instance.message,
    #             'sent': form.instance.sent,
    #             'errors': form.errors
    #         }
    #         request.session['form'] = form

    #     return HttpResponseRedirect(referer)

    def post(self, request, *args, **kwargs):
        form = ContactUsForm(json.loads(request.body.decode('utf-8')))
        data = {
            'data': '',
            'ok': False,
            'errors': {},
        }
        if form.is_valid():
            form.save()
            contact_us = form.send_mail()

            data['data'] = model_to_dict(contact_us)
            data['ok'] = True
        else:
            data['errors'] = form.errors

        return JsonResponse(data)


class SubscribeView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = {
            'ok': False
        }
        return JsonResponse(data)
