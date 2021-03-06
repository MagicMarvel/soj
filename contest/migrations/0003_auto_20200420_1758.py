# Generated by Django 2.2.9 on 2020-04-20 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20200315_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='password',
            field=models.CharField(blank=True, help_text='only used if category is PRIVATE', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contest',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='registered users or entered-password users', to=settings.AUTH_USER_MODEL),
        ),
    ]
