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
