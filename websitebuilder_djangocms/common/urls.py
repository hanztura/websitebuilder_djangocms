from django.urls import path

from .views import ContactUsFormView, SubscribeView

app_name = 'common'
urlpatterns = [
    path('contact-us/', ContactUsFormView.as_view(), name='contact_us'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
