from django.contrib import admin

from events.models import Event, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'start_date', 'end_date','category')
