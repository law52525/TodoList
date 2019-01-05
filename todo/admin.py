from django.contrib import admin
from todo.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_text']}),
        ('日期', {'fields': ['create_date']})
    ]
    list_display = ('task_text', 'create_date', 'was_created_recently')
    list_filter = ['create_date']
    search_fields = ['task_text']
    list_per_page = 7


admin.site.register(Task, TaskAdmin)
