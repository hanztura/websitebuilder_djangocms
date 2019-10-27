from django.db import models


class BasicLinkMixin(models.Model):
    text = models.CharField(max_length=50)
    href = models.CharField(max_length=1000, blank=True, default='#')

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


class InsertInstanceOnContextPlugin:

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
