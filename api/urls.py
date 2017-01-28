from django.conf.urls import include, url
from rest_framework import routers

from comic.viewsets import *

router = routers.DefaultRouter()
router.register(r'comic', ComicViewSet)
router.register(r'cast', CastViewSet)
router.register(r'headerimage', HeaderImageViewSet)
router.register(r'issue', IssueViewSet)

urlpatterns = [
            url(r'^comic/(?P<issueId>\d+)/(?P<pageNumber>\d+)/', IssuePageViewSet.as_view()),
            url(r'^', include(router.urls)),
]





