from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import User
from management.models import Task

# Register your models here.

class TaskInline(admin.TabularInline):
    model = Task
    fields = ['name', 'status']

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
      model = User
      fields = ('email', 'name', 'lastname')

    def clean_password2(self):
      password1 = self.cleaned_data.get("password1")
      password2 = self.cleaned_data.get("password2")
      if password1 and password2 and password1 != password2:
          raise ValidationError("Passwords don't match")
      return password2

    def save(self, commit=True):
      user = super().save(commit=False)
      user.set_password(self.cleaned_data["password1"])
      if commit:
          user.save()
      return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
      model = User
      fields = ('email', 'password', 'name', 'lastname', 'is_active', 'is_staff')

# class UserAdmin(admin.ModelAdmin):
class UserAdmin(BaseUserAdmin):
  # fields = ['name', 'lastname', 'email', 'password', 'is_staff', 'is_active', 'is_superuser']

  form = UserChangeForm
  add_form = UserCreationForm

  list_display = ('email', 'name', 'is_staff', 'is_superuser')
  list_filter = ('is_staff','is_superuser',)

  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', 'lastname')}),
      ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
  
  add_fieldsets = (
      (None, {
        'classes': ('wide',),
        'fields': ('email', 'name', 'lastname', 'password1', 'password2'),
      }),
    )
  
  search_fields = ('email',)
  ordering = ('email',)
  filter_horizontal = ()

  inlines = [
      TaskInline,
    ]
  
  def has_add_permission(self, request, obj=None):
    return request.user.is_superuser

  def has_delete_permission(self, request, obj=None):
    return request.user.is_superuser
  
  def has_change_permission(self, request, obj=None):
    # return request.user.is_superuser or (obj and obj.id == request.user.id)
    return request.user.is_superuser

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)