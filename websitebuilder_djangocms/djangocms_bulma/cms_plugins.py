from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ButtonPluginModel, NavbarPluginModel


@plugin_pool.register_plugin
class NavbarPluginPublisher(CMSPluginBase):
    model = NavbarPluginModel
    module = 'Bulma'
    name = 'Navbar Plugin'
    render_template = 'djangocms_bulma/navbar.html'

    def render(self, context, instance, placeholder):
        items = instance.items.all()
        context.update({'instance': instance, 'items': items})

        return context


@plugin_pool.register_plugin
class ButtonPluginPublisher(CMSPluginBase):
    model = ButtonPluginModel
    module = 'Bulma'
    name = 'Button Plugin'
    render_template = 'djangocms_bulma/button.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context
