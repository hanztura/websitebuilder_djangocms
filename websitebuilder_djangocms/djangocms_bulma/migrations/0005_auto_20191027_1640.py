# Generated by Django 2.2.6 on 2019-10-27 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_bulma', '0004_buttonpluginmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buttonpluginmodel',
            old_name='_class',
            new_name='html_class',
        ),
    ]
