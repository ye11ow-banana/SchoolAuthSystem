# Generated by Django 4.1.3 on 2022-12-05 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Id of extension type. E.g. id of `TeacherType`'),
        ),
        migrations.AlterField(
            model_name='workerlist',
            name='token_expiration_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 5, 19, 9, 9, 194464), verbose_name='Expiration date of token'),
        ),
    ]
