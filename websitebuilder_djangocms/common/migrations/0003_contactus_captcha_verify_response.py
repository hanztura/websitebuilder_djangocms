# Generated by Django 2.2.6 on 2019-10-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20191030_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='captcha_verify_response',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
