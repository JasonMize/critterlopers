from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializers import *

from pprint import pprint

import traceback

class ComicViewSet(viewsets.ModelViewSet):
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


    def retrieve(self, request, pageNumber):
        try:
            sortOrder = Comic.sortOrder(pageNumber)
            queryset = Comic.objects.filter(page_number=int(pageNumber))
            comic = get_object_or_404(queryset)
            serializer = ComicSerializer(comic)

            info = serializer.data

        except:
            # reroute non-page to the last page
            default_comic = Comic.objects.filter(page_number=1)
            last_page = default_comic[0].last_page
            sortOrder = Comic.sortOrder(last_page)
            queryset = Comic.objects.filter(page_number = last_page)
            comic = get_object_or_404(queryset)
            serializer = ComicSerializer(comic)

            info = serializer.data

        finally:
            return Response(info)


