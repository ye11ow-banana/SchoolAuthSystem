from django.contrib import admin

from salary_info.models import (
    SalaryHistory, TeacherSalaryInfo,
    SecurityGuardSalaryInfo, CookSalaryInfo
)


@admin.register(SalaryHistory)
class SalaryHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'worker_id', 'income_amount', 'start_date', 'end_date'
    )
    list_display_links = 'worker_id',
    list_filter = 'worker_id', 'start_date', 'end_date'
    search_fields = 'worker_id',
    save_on_top = True
    save_as = True


@admin.register(TeacherSalaryInfo)
class TeacherSalaryInfoAdmin(admin.ModelAdmin):
    list_display = (
        'course_increase', 'service_years', 'service_years_increase',
        'classroom_increase', 'seniors_group_increase',
        'juniors_group_increase', 'checking_notebooks_increase',
        'students_number_needed_for_increase_for_checking_notebooks'
    )
    save_on_top = True
    save_as = True


@admin.register(SecurityGuardSalaryInfo)
class SecurityGuardSalaryInfoAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True


@admin.register(CookSalaryInfo)
class CookSalaryInfoAdmin(admin.ModelAdmin):
    list_display = 'chief_increase',
    save_on_top = True
    save_as = True
