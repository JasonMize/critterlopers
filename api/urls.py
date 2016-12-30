from django.conf.urls import include, url
from rest_framework import routers

from comic.viewsets import *

router = routers.DefaultRouter()
router.register(r'comic', ComicViewSet)
router.register(r'comic', CastViewSet)
router.register(r'headerimage', HeaderImageViewSet)

urlpatterns = [
            url(r'^', include(router.urls)), 
]





