
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import RedirectView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^comic/', include('comic.urls')),
    url(r'^api/', include('api.urls')),
    # TODO make last page update automatically
    url(r'^$', RedirectView.as_view(url='/comic/38', permanent=False)),
    url(r'^', include('core.urls')),
]


