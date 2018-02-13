from django.conf.urls import include, url
from rest_framework import routers

from comic.viewsets import *

router = routers.DefaultRouter()
router.register(r'comic', ComicViewSet)
# router.register(r'cast', CastViewSet)
router.register(r'headerimage', HeaderImageViewSet)
router.register(r'issue', IssueViewSet)

urlpatterns = [
    url(r'^comic/$', 
        IssueComicViewSet.as_view({'get': 'list'})
    ),
    url(r'^comic/(?P<pageNumber>\d+)/$', 
        IssueComicViewSet.as_view({'get': 'retrieve'})
    ),
    url(r'^comic/(?P<pageNumber>\d+)/(?P<navigation>prev|next|first|last)$', 
        IssueComicViewSet.as_view({'get': 'retrieve'})
    ),
    url(r'^', include(router.urls)),
]





