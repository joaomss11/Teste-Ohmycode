from django.contrib import admin
from .models import Task, User

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    #[field.name for field in User._meta.fields if field.name != "id"]


# Register your models here.
