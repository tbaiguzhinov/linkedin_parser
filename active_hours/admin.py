from django.contrib import admin
from active_hours.models import Contact, Presence


class PresenceInlines(admin.TabularInline):
    model = Presence
    extra = 0
    readonly_fields = ['current_time', 'status']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [PresenceInlines]
    ordering = ['full_name']
    list_display = ['full_name', 'logins_counted']
    readonly_fields = ['full_name', 'occupation']

    def logins_counted(self, obj):
        return obj.presence_hours.count()


@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_filter = ['status']
