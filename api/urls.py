from django.conf.urls import include, url
from rest_framework import routers

from comic.viewsets import ComicViewSet

router = routers.DefaultRouter()
router.register(r'comic', ComicViewSet)

urlpatterns = [
            url(r'^', include(router.urls)), 
]





