from django.contrib import admin

from .models import Comic

class ComicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

admin.site.register(Comic, ComicAdmin)