from rest_framework import viewsets

from .models import *
from .serializers import *

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.order_by('-sort_number', '-issue', '-page_number', '-date_added').all()
    serializer_class = ComicSerializer

class IssuePageViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Comic.objects.all()
        comic = get_object_or_404(queryset, issue_id=self.kwargs.issueId, page_number=self.kwargs.pageNumber)
        serializer = ComicSerializer(comic)
        return Response(serializer.data)

class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class HeaderImageViewSet(viewsets.ModelViewSet):
    queryset = HeaderImage.objects.all()
    serializer_class = HeaderImageSerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

