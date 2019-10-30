from django.urls import path

from .views import ContactUsFormView

app_name = 'common'
urlpatterns = [
    path('contact-us/', ContactUsFormView.as_view(), name='contact_us')
]
