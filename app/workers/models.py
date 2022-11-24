import binascii
import os
from datetime import datetime, timedelta

from django.db import models


class WorkerList(models.Model):
    """
    List of school workers.

    User can create many WorkerLists for different
    schools with different workers.
    """
    title = models.CharField(
        'Title of worker list', default='My Worker List', max_length=255)
    token = models.CharField(
        'Access token to worker list', max_length=40, null=True)
    token_expiration_date = models.DateTimeField(
        'Expiration date of token', default=datetime.now() + timedelta(hours=3))
    creation_date = models.DateField('Creation date', auto_now_add=True)

    class Meta:
        db_table = 'worker_list'
        verbose_name = 'worker list'
        verbose_name_plural = 'worker lists'

    def __str__(self) -> str:
        return str(self.title)

    @staticmethod
    def generate_token() -> str:
        return binascii.hexlify(os.urandom(20)).decode()


class AbstractWorker(models.Model):
    """
    School employee.

    Worker has common fields for all types. There are many types
    of worker. For example, teacher or cook.
    They have some special fields for their classes.
    """
    JOB_TITLE = (
        ('teacher', 'teacher'),
        ('cook', 'cook'),
        ('security', 'security')
    )
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
        WorkerList, on_delete=models.CASCADE, verbose_name='Worker list')
    add_date = models.DateField('Date of first creating', auto_now_add=True)
    title = models.CharField('Job title', choices=JOB_TITLE, max_length=50)
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

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Teacher(AbstractWorker):
    """
    Worker type that teaches students at school.
    """
    salary_info = models.ForeignKey(
        'salary_info.TeacherSalaryInfo', on_delete=models.CASCADE,
        verbose_name='Model with fields for salary calculation'
    )
    completed_courses = models.PositiveSmallIntegerField(
        'Number of advanced training courses completed', default=0)
    has_classroom = models.BooleanField(
        'Teacher has classroom', default=False)
    subjects = models.ManyToManyField(
        'students.Subject', related_name='Subjects')

    class Meta:
        db_table = 'teacher'
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class SecurityGuard(AbstractWorker):
    """
    Worker type that keeps an eye on security at school.
    """
    salary_info = models.ForeignKey(
        'salary_info.SecurityGuardSalaryInfo', on_delete=models.CASCADE,
        verbose_name='Model with fields for salary calculation'
    )

    class Meta:
        db_table = 'security_guard'
        verbose_name = 'security guard'
        verbose_name_plural = 'security guards'


class Cook(AbstractWorker):
    """
    Worker type that cooks food at school.
    """
    salary_info = models.ForeignKey(
        'salary_info.CookSalaryInfo', on_delete=models.CASCADE,
        verbose_name='Model with fields for salary calculation'
    )
    is_chief = models.BooleanField('Is chief cook', default=False)

    class Meta:
        db_table = 'cook'
        verbose_name = 'cook'
        verbose_name_plural = 'cooks'
