# Generated by Django 2.2.6 on 2019-10-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_bulma', '0012_auto_20191027_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='heropluginmodel',
            name='html_class',
            field=models.CharField(blank=True, max_length=1000, verbose_name='class'),
        ),
    ]