from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import (
    ButtonPluginModel, CardPluginModel, HeroPluginModel, NavbarPluginModel)


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


@plugin_pool.register_plugin
class CardPluginPublisher(CMSPluginBase):
    model = CardPluginModel
    module = 'Bulma'
    name = 'Card Plugin'
    render_template = 'djangocms_bulma/card.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context


@plugin_pool.register_plugin
class HeroPluginPublisher(CMSPluginBase):
    model = HeroPluginModel
    module = 'Bulma'
    name = 'Hero Plugin'
    render_template = 'djangocms_bulma/hero.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})

        return context
