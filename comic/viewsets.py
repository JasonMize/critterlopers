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

            tb = serializer.data
        except:
            tb = traceback.format_exc()

        finally:
            return Response(tb)

# "Traceback (most recent call last):
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/backends/utils.py\", line 65, in execute
#     return self.cursor.execute(sql, params)
# psycopg2.ProgrammingError: operator does not exist: character varying = integer
# LINE 1: ...d\" FROM \"comic_comic\" WHERE \"comic_comic\".\"page_number\" = 38
#                                                                    ^
# HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.


# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File \"/opt/python/current/app/comic/viewsets.py\", line 43, in retrieve
#     comic = get_object_or_404(queryset)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/shortcuts.py\", line 85, in get_object_or_404
#     return queryset.get(*args, **kwargs)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/models/query.py\", line 374, in get
#     num = len(clone)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/models/query.py\", line 232, in __len__
#     self._fetch_all()
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/models/query.py\", line 1118, in _fetch_all
#     self._result_cache = list(self._iterable_class(self))
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/models/query.py\", line 53, in __iter__
#     results = compiler.execute_sql(chunked_fetch=self.chunked_fetch)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/models/sql/compiler.py\", line 886, in execute_sql
#     raise original_exception
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/models/sql/compiler.py\", line 876, in execute_sql
#     cursor.execute(sql, params)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/backends/utils.py\", line 65, in execute
#     return self.cursor.execute(sql, params)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/utils.py\", line 94, in __exit__
#     six.reraise(dj_exc_type, dj_exc_value, traceback)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/utils/six.py\", line 685, in reraise
#     raise value.with_traceback(tb)
#   File \"/opt/python/run/venv/local/lib/python3.6/site-packages/django/db/backends/utils.py\", line 65, in execute
#     return self.cursor.execute(sql, params)
# django.db.utils.ProgrammingError: operator does not exist: character varying = integer
# LINE 1: ...d\" FROM \"comic_comic\" WHERE \"comic_comic\".\"page_number\" = 38
#                                                                    ^
# HINT:  No operator matches the given name and argument type(s). You might need to add explicit type casts.

# "






