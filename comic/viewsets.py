from rest_framework import viewsets

from .models import Comic, HeaderImage
from .serializers import ComicSerializer, HeaderImageSerializer

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer

class HeaderImageViewSet(viewsets.ModelViewSet):
    queryset = HeaderImage.objects.all()
    serializer_class = HeaderImageSerializer
