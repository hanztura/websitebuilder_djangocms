from django.db import models

from cms.models import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField

from .utils import BasicLinkMixin, LabelFieldMixin


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


class CardPluginModel(LabelFieldMixin, CMSPlugin):
    image = FilerImageField(null=True, blank=True, on_delete=models.PROTECT)
    content = HTMLField(blank=True)


class HeroPluginModel(LabelFieldMixin, CMSPlugin):
    full_height = models.BooleanField(default=True, blank=True)
    with_navbar = models.BooleanField(default=False, blank=True)
    content = HTMLField()
    html_class = models.CharField(
        max_length=1000, blank=True, verbose_name='class')

    @property
    def fullheight_class(self):
        class_value = ''

        if self.full_height:
            class_value = 'is-fullheight'
            if self.with_navbar:
                class_value = 'is-fullheight-with-navbar'

        return class_value
