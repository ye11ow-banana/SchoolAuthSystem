# Generated by Django 4.1.4 on 2022-12-17 18:02

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workers', '0006_alter_worker_worker_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerlist',
            name='users',
        ),
        migrations.AddField(
            model_name='workerlist',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='owners'),
        ),
        migrations.AlterField(
            model_name='workerlist',
            name='token_expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 17, 21, 1, 51, 949563), verbose_name='Expiration date of token'),
        ),
    ]
