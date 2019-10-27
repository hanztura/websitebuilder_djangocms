from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from .utils import BasicLinkMixin


class Link(BasicLinkMixin):
    pass


class NavbarPluginModel(CMSPlugin):
    brand_image = FilerImageField(
        null=True, blank=True, on_delete=models.SET_NULL)
    brand_text = models.CharField(max_length=100)
    items = models.ManyToManyField(Link)

    def __str___(self):
        return self.brand_text

    def copy_relations(self, oldinstance):
        self.items.set(oldinstance.items.all())


class ButtonPluginModel(CMSPlugin):
    text = models.TextField()
    link = models.CharField(max_length=1200, blank=True)
    html_class = models.CharField(
        max_length=1000, blank=True, default='button', verbose_name='class',
        help_text='Class attribute values. separated with space.')

    def __str__(self):
        return self.text
