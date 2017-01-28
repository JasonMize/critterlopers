from rest_framework import viewsets

from .models import *
from .serializers import *

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.order_by('-sort_number', '-issue', '-page_number', '-date_added').all()
    serializer_class = ComicSerializer

class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class HeaderImageViewSet(viewsets.ModelViewSet):
    queryset = HeaderImage.objects.all()
    serializer_class = HeaderImageSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

