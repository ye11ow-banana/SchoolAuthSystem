# Generated by Django 4.1.3 on 2022-12-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workersalaryinfo',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Id of extension type. E.g. id of `TeacherTypeSalaryInfo`'),
        ),
    ]
