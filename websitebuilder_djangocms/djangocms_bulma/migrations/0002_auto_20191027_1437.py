# Generated by Django 2.2.6 on 2019-10-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_bulma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='href',
            field=models.CharField(blank=True, default='#', max_length=1000),
        ),
    ]
