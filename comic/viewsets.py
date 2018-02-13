from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializers import *

class ComicViewSet(viewsets.ModelViewSet):
    print('VIEWSETS: COMIC VIEW SET: ')
    queryset = Comic.objects.order_by(
        '-sort_number', 
        '-issue', 
        '-page_number', 
        '-date_added'
    ).all()
    serializer_class = ComicSerializer

# class CastViewSet(viewsets.ModelViewSet):
#     queryset = Cast.objects.all()
#     serializer_class = CastSerializer

class HeaderImageViewSet(viewsets.ModelViewSet):
    queryset = HeaderImage.objects.all()
    serializer_class = HeaderImageSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueComicViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Comic.objects.all()
        serializer = ComicSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pageNumber, navigation=None):
        sortOrder = Comic.sortOrder(pageNumber)
        if navigation == 'prev':
            queryset = Comic.objects.order_by('-sort_number').filter(sort_number__lt=sortOrder)[:1]
        elif navigation == 'next':
            queryset = Comic.objects.order_by('sort_number').filter(sort_number__gt=sortOrder)[:1]
        elif navigation == 'first':
            queryset = Comic.objects.order_by('sort_number').all()[:1]
        elif navigation == 'last':
            queryset = Comic.objects.order_by('-sort_number').all()[:1]
        else:
            queryset = Comic.objects.filter(page_number=pageNumber).all()

        comics = get_object_or_404(queryset)
        serializer = ComicSerializer(comics)
        return Response(serializer.data)


