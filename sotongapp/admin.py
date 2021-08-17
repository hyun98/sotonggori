from django.contrib import admin
from sotongapp.models import Information, Organ


class OrganAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'urlname'
    )
    list_display_links = (
        'name', 'urlname'
    )

class InformationAdmin(admin.ModelAdmin):
    list_display = (
        'temp', 'day', 'time', 'organ__name'
    )
    list_display_links = (
        'temp', 'day', 'time', 'organ__name'
    )
    list_filter = (
        'day', 'organ__name',
    )

admin.site.register(Organ, OrganAdmin)
admin.site.register(Information, InformationAdmin)