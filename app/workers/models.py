import binascii
import os
from datetime import datetime, timedelta

from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class WorkerList(models.Model):
    """
    List of school workers.

    User can create many WorkerLists for different
    schools with different workers.
    """
    title = models.CharField(
        'Title of worker list', default='My Worker List', max_length=255)
    token = models.CharField(
        'Access token to worker list', max_length=40, null=True, blank=True)
    token_expiration_date = models.DateTimeField(
        'Expiration date of token', default=datetime.now() + timedelta(hours=3), blank=True)
    creation_date = models.DateField('Creation date', auto_now_add=True, blank=True)
    users = models.ManyToManyField(AUTH_USER_MODEL, verbose_name='')

    class Meta:
        db_table = 'worker_list'
        verbose_name = 'worker list'
        verbose_name_plural = 'worker lists'

    def __str__(self) -> str:
        return str(self.title)

    def get_absolute_url(self) -> str:
        return reverse('workers:worker_list', args=[self.pk], current_app='workers')

    @staticmethod
    def generate_token() -> str:
        return binascii.hexlify(os.urandom(20)).decode()


class Worker(models.Model):
    """
    School employee.

    An ordinary employee who has no additional fields,
    except for those common to everyone.
    For example, a security guard. He has a name and an age.

    There are also regular employee extensions (`extension_type`).
    For example, a `TeacherType` model. Teacher may have his own class,
    as well as a list of subjects he teaches.
    """
    STATUS = (
        ('active', 'active'),
        ('time_off', 'time off'),
        ('vacation', 'vacation'),
        ('overtime', 'overtime'),
        ('sick', 'sick'),
        ('decree', 'decree')
    )

    first_name = models.CharField('First name', max_length=50)
    middle_name = models.CharField('Middle name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    birth_date = models.DateField('Birth date')
    worker_list = models.ForeignKey(
        WorkerList, on_delete=models.CASCADE,
        verbose_name='Worker list', related_name='workers'
    )
    add_date = models.DateField('Date of first creating', auto_now_add=True)
    job_title = models.CharField('Job title', max_length=255)
    status = models.CharField(
        'Working status', choices=STATUS,
        default='active', max_length=50
    )
    months_experience = models.PositiveSmallIntegerField(
        'Number of months of experience', default=0)
    wage_rate = models.DecimalField(
        'The rate for which the employee works',
        max_digits=3, decimal_places=2, default=1
    )
    wage_rate_salary = models.PositiveIntegerField(
        'Salary for one job', default=6000
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='Worker extension. Like a teacher or a cook. '
                     'Leave blank if this is a regular employee'
    )
    object_id = models.PositiveIntegerField(
        'Id of extension type. E.g. id of `TeacherType`', null=True, blank=True)
    extension_type = GenericForeignKey()
    salary_info = models.ForeignKey(
        'salary_info.WorkerSalaryInfo', on_delete=models.DO_NOTHING,
        verbose_name='Model with fields for salary calculation'
    )

    class Meta:
        db_table = 'worker'
        verbose_name = 'worker'
        verbose_name_plural = 'workers'
        unique_together = 'content_type', 'object_id'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class TeacherType(models.Model):
    """
    Extension type of worker that teaches students at school.
    """
    completed_courses = models.PositiveSmallIntegerField(
        'Number of advanced training courses completed', default=0)
    has_classroom = models.BooleanField(
        'Teacher has classroom', default=False)
    subjects = models.ManyToManyField(
        'students.Subject', verbose_name='Subjects')
    worker = GenericRelation(Worker)

    class Meta:
        db_table = 'teacher'
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class CookType(models.Model):
    """
    Extension type of worker that cooks food at school.
    """
    is_chief = models.BooleanField('Is chief cook', default=False)
    worker = GenericRelation(Worker)

    class Meta:
        db_table = 'cook'
        verbose_name = 'cook'
        verbose_name_plural = 'cooks'
