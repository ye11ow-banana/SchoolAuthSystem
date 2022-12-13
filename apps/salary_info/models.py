from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class SalaryHistory(models.Model):
    """
    Data about amount of income and (Worker model
    and its types fields) within period of time.

    Example: from `09.11.2022` to `15.11.2022` worker
    earns 15_000 being status=`sick`.
    """
    worker_id = models.PositiveSmallIntegerField('Worker id')
    income_amount = models.PositiveIntegerField(
        'Amount of income for period', default=0)
    start_date = models.DateField(
        'Date that starts period', auto_now_add=True)
    end_date = models.DateField(
        'Date that ends period', auto_now=True)
    saved_state = models.JSONField(
        'Saving state of fields of worker model and its type')

    class Meta:
        db_table = 'salary_history'
        verbose_name = 'salary history'
        verbose_name_plural = 'salary histories'

    def __str__(self) -> str:
        return f'{self.start_date} - {self.end_date}'

    @staticmethod
    def get_state() -> str:
        raise NotImplementedError('Return JSON state of the object!')


class AbstractWorkerSalaryInfo(models.Model):
    """
    Abstract class for all salary supplements classes.
    """
    class Meta:
        abstract = True

    def calculate_salary(self):
        raise NotImplementedError('Calculate salary for regular worker!')


class WorkerSalaryInfo(AbstractWorkerSalaryInfo):
    """
    Salary supplements for regular Worker.
    """
    title = models.CharField('Title', max_length=255)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='Salary info extension. Like salary info about a teacher or a cook. '
                     'Leave blank if this is salary info for a regular employee'
    )
    object_id = models.PositiveIntegerField(
        'Id of extension type. E.g. id of `TeacherTypeSalaryInfo`', null=True, blank=True)
    extension_type = GenericForeignKey()

    class Meta:
        db_table = 'worker_salary_info'
        verbose_name = 'worker salary info'
        verbose_name_plural = 'worker salary infos'
        unique_together = 'content_type', 'object_id'

    def __str__(self) -> str:
        return f'Salary info: {self.title}'

    def calculate_salary(self):
        raise NotImplementedError


class TeacherTypeSalaryInfo(AbstractWorkerSalaryInfo):
    """
    Salary supplements for Teacher type.
    """
    course_increase = models.PositiveSmallIntegerField(
        'Salary increase for course', default=150)
    service_years = models.PositiveSmallIntegerField(
        'Years of service to increase salary', default=3
    )
    service_years_increase = models.PositiveSmallIntegerField(
        'Percentage of salary increase for years of service', default=10
    )
    classroom_increase = models.PositiveSmallIntegerField(
        'Percentage of salary increase for having classroom', default=10
    )
    seniors_group_increase = models.PositiveSmallIntegerField(
        'Percentage of salary increase for supervise seniors group',
        default=25
    )
    juniors_group_increase = models.PositiveSmallIntegerField(
        'Percentage of salary increase for supervise juniors group',
        default=20
    )
    checking_notebooks_subjects = models.ManyToManyField(
        'students.Subject', verbose_name='Subjects for salary increase '
        'for checking notebooks'
    )
    checking_notebooks_increase = models.PositiveSmallIntegerField(
        'Percentage of salary increase for checking notebooks',
        default=10
    )
    students_number_needed_for_increase_for_checking_notebooks = \
        models.PositiveSmallIntegerField(
            'Number of students needed for salary increase '
            'for checking notebooks',
            default=12
        )
    worker_salary_info = GenericRelation(WorkerSalaryInfo)

    class Meta:
        db_table = 'teacher_salary_info'
        verbose_name = 'teacher salary info'
        verbose_name_plural = 'teacher salary infos'

    def calculate_salary(self):
        raise NotImplementedError


class CookTypeSalaryInfo(AbstractWorkerSalaryInfo):
    """
    Salary supplements for Cook type.
    """
    chief_increase = models.PositiveSmallIntegerField(
        'Salary increase for chief cook', default=2000)
    worker_salary_info = GenericRelation(WorkerSalaryInfo)

    class Meta:
        db_table = 'cook_salary_info'
        verbose_name = 'cook salary info'
        verbose_name_plural = 'cook salary infos'

    def calculate_salary(self):
        raise NotImplementedError
