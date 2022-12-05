from django.contrib import admin

from .models import WorkerList, Worker, TeacherType, CookType


@admin.register(WorkerList)
class WorkerListAdmin(admin.ModelAdmin):
    list_display = 'title', 'creation_date'
    search_fields = 'title',
    readonly_fields = 'token', 'token_expiration_date', 'creation_date'
    save_on_top = True
    save_as = True
    fields = ('title', 'creation_date'),


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'middle_name', 'last_name', 'birth_date',
        'worker_list', 'add_date', 'job_title', 'salary_info',
        'status', 'months_experience', 'wage_rate', 'wage_rate_salary',
        'content_type', 'object_id', 'extension_type'
    )
    list_display_links = (
        'first_name', 'middle_name', 'last_name', 'status'
    )
    list_filter = (
        'job_title', 'status', 'months_experience', 'wage_rate'
    )
    search_fields = 'first_name', 'middle_name', 'last_name'
    save_on_top = True
    save_as = True


@admin.register(TeacherType)
class TeacherTypeAdmin(admin.ModelAdmin):
    list_display = 'completed_courses', 'has_classroom'
    list_display_links = 'has_classroom',
    list_filter = 'has_classroom',
    save_on_top = True
    save_as = True


@admin.register(CookType)
class CookTypeAdmin(admin.ModelAdmin):
    list_display = 'is_chief',
    list_display_links = 'is_chief',
    list_filter = 'is_chief',
    save_on_top = True
    save_as = True


admin.site.site_title = 'System'
admin.site.site_header = 'System'
