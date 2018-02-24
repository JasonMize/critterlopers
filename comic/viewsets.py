from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import *
from .serializers import *

from pprint import pprint

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
        print('PAGE NUMBER: ', pageNumber)
        print('REQUEST: ', request)
        # pprint(dir(request))

        print('SELF: ', self)

        # import traceback

        # try:
        #     raise ValueError
        # except:
        #     tb = traceback.format_exc()
        # else:
        #     tb = "No error"
        # finally:
        #     print (tb)

        sortOrder = Comic.sortOrder(pageNumber)
        queryset = Comic.objects.filter(page_number=pageNumber)
        print('QUERYSET: ')
        pprint(queryset)
        comic = get_object_or_404(queryset)
        serializer = ComicSerializer(comic)

        return Response(serializer.data)


