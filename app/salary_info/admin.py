from django.contrib import admin

from salary_info.models import (
    SalaryHistory, WorkerSalaryInfo,
    TeacherTypeSalaryInfo, CookTypeSalaryInfo
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


@admin.register(WorkerSalaryInfo)
class WorkerSalaryInfoAdmin(admin.ModelAdmin):
    list_display = 'title', 'content_type', 'object_id', 'extension_type'
    list_display_links = 'title',
    search_fields = 'title',
    fields = 'title', 'content_type', 'object_id', 'extension_type'
    readonly_fields = 'extension_type',
    save_on_top = True
    save_as = True


@admin.register(TeacherTypeSalaryInfo)
class TeacherTypeSalaryInfoAdmin(admin.ModelAdmin):
    list_display = (
        'course_increase', 'service_years', 'service_years_increase',
        'classroom_increase', 'seniors_group_increase',
        'juniors_group_increase', 'checking_notebooks_increase',
        'students_number_needed_for_increase_for_checking_notebooks'
    )
    save_on_top = True
    save_as = True


@admin.register(CookTypeSalaryInfo)
class CookTypeSalaryInfoAdmin(admin.ModelAdmin):
    list_display = 'chief_increase',
    save_on_top = True
    save_as = True
