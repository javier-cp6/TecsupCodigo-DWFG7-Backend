from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'status', 'userId']

  list_filter = ('userId','status',)

  def has_add_permission(self, request, obj=None):
    return request.user.is_superuser

  def has_delete_permission(self, request, obj=None):
    return request.user.is_superuser
  
  def has_change_permission(self, request, obj=None):
    return request.user.is_superuser

admin.site.register(Task, TaskAdmin)