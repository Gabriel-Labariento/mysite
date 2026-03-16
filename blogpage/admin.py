from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Task, TaskGroup, Profile

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline, ]

class TaskInline(admin.TabularInline):
    model = Task

class TaskGroupAdmin(admin.ModelAdmin):
    model = TaskGroup
    inlines = [TaskInline]

class TaskAdmin(admin.ModelAdmin):
    model = Task

    search_fields = ['name']

    list_display = ('name', 'due_date')

    list_filter = ('name', 'due_date')

    fieldsets = [
        ('Details', {
            'fields': [
                ('name', 'due_date'), 'taskgroup', 'profile', 'task_image'
            ]
        })
    ]

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)