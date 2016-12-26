from django.contrib import admin

from .models import Comic, HeaderImage

class ComicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
    )

class HeaderImageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'image',
    )

admin.site.register(Comic, ComicAdmin)
admin.site.register(HeaderImage, HeaderImageAdmin)