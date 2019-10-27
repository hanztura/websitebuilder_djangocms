# Generated by Django 2.2.6 on 2019-10-27 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('djangocms_bulma', '0003_auto_20191027_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_bulma_buttonpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('text', models.TextField()),
                ('link', models.CharField(blank=True, max_length=1200)),
                ('_class', models.CharField(blank=True, default='button', help_text='Class attribute values. separated with space.', max_length=1000, verbose_name='class')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]