from django.contrib import admin
from .models import TodoItem

# Register your models here.

#Admin changelist 
@admin.action(description="Mark selected items' status as Open")
def make_Open(modeladmin, request, queryset):
    queryset.update(status='OPEN')
@admin.action(description="Mark selected items' status as Working")
def make_Working(modeladmin, request, queryset):
    queryset.update(status='WORKING')
@admin.action(description="Mark selected items' status as Done")
def make_Done(modeladmin, request, queryset):
    queryset.update(status='DONE')
@admin.action(description="Mark selected items' status as Overdue")
def make_Overdue(modeladmin, request, queryset):
    queryset.update(status='OVERDUE')

# @admin.register(TodoItem)     #using decorator
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ["title", "due_date", "status"]
    # ordering = ["title"]
    date_hierarchy = "timestamp"
    actions = [make_Open, make_Working, make_Done, make_Overdue]
    empty_value_display = "-empty-"
    # list_filter = ["title", "due_date", "tags", "status"]

    fieldsets = [
        (
            None,
            {
                "fields":["title", "description"],
            },
        ),
        (
            None,
            {
                "fields": ["tags", "status"]
            }
        ),
        (
            "Dates :",
            {
                "classes": ["collapse"],
                "fields": ["timestamp", "due_date"],
            }
        ),
    ]

admin.site.register(TodoItem, TodoItemAdmin)
