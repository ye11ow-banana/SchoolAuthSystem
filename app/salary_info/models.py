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
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'Salary info of {self.pk} pk'

    def calculate_salary(self):
        raise NotImplementedError('Calculate salary for regular worker!')


class TeacherSalaryInfo(AbstractWorkerSalaryInfo):
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

    class Meta:
        db_table = 'teacher_salary_info'
        verbose_name = 'teacher salary info'
        verbose_name_plural = 'teacher salary infos'

    def calculate_salary(self):
        raise NotImplementedError


class SecurityGuardSalaryInfo(AbstractWorkerSalaryInfo):
    """
    Salary supplements for SecurityGuard type.
    """
    class Meta:
        db_table = 'security_guard_salary_info'
        verbose_name = 'security guard salary info'
        verbose_name_plural = 'security guard salary infos'

    def calculate_salary(self):
        raise NotImplementedError


class CookSalaryInfo(AbstractWorkerSalaryInfo):
    """
    Salary supplements for Cook type.
    """
    chief_increase = models.PositiveSmallIntegerField(
        'Salary increase for chief cook', default=2000)

    class Meta:
        db_table = 'cook_salary_info'
        verbose_name = 'cook salary info'
        verbose_name_plural = 'cook salary infos'

    def calculate_salary(self):
        raise NotImplementedError
