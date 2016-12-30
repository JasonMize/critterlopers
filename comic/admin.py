from django.contrib import admin

from .models import *

class ComicAdmin(admin.ModelAdmin):
    list_display = (
        'page_number',
        'title',
        'issue',
        'image',
        'date_added',
    )

class CastAdmin(admin.ModelAdmin):
    list_display = (
        'name',
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