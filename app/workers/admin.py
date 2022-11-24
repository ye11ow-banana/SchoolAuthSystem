from django.contrib import admin

from .models import WorkerList, Teacher, SecurityGuard, Cook


@admin.register(WorkerList)
class WorkerListAdmin(admin.ModelAdmin):
    list_display = 'title', 'creation_date'
    search_fields = 'title',
    readonly_fields = 'token', 'token_expiration_date', 'creation_date'
    save_on_top = True
    save_as = True
    fields = ('title', 'creation_date'),


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'birth_date',
        'worker_list', 'add_date', 'title', 'salary_info',
        'completed_courses', 'has_classroom', 'status',
        'months_experience', 'wage_rate', 'wage_rate_salary'
    )
    list_display_links = (
        'first_name', 'middle_name', 'last_name', 'status'
    )
    list_filter = (
        'has_classroom', 'title', 'status',
        'months_experience', 'wage_rate'
    )
    search_fields = 'first_name', 'middle_name', 'last_name'
    save_on_top = True
    save_as = True


@admin.register(SecurityGuard)
class SecurityGuardAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'birth_date',
        'worker_list', 'add_date', 'title', 'salary_info',
        'status', 'months_experience', 'wage_rate', 'wage_rate_salary'
    )
    list_display_links = (
        'first_name', 'middle_name', 'last_name', 'status'
    )
    list_filter = 'title', 'status', 'months_experience', 'wage_rate'
    search_fields = 'first_name', 'middle_name', 'last_name'
    save_on_top = True
    save_as = True


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'birth_date',
        'worker_list', 'add_date', 'title', 'salary_info', 'is_chief',
        'status', 'months_experience', 'wage_rate', 'wage_rate_salary'
    )
    list_display_links = (
        'first_name', 'middle_name', 'last_name', 'status'
    )
    list_filter = (
        'title', 'is_chief', 'status',
        'months_experience', 'wage_rate'
    )
    search_fields = 'first_name', 'middle_name', 'last_name'
    save_on_top = True
    save_as = True


admin.site.site_title = 'System'
admin.site.site_header = 'System'
