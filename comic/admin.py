from django.contrib import admin

from .models import *


class ComicAdmin(admin.ModelAdmin):
    list_display = (
        'sort_number',
        'issue',
        'page_number',
        'title',
        'image',
        'date_added',
    )


class CastAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
    )


class HeaderImageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'image',
    )

admin.site.register(Comic, ComicAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(HeaderImage, HeaderImageAdmin)