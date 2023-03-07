from django.contrib import admin

from webapp.models import Issue, Type, Status


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at')
    search_fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at')
    fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Issue, IssueAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id',)


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id',)


admin.site.register(Status, StatusAdmin)
