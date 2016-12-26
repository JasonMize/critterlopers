from rest_framework import serializers

from .models import Comic, HeaderImage

class ComicSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Comic
        fields = (
            'id',
            'title',
            'image',
        )

class HeaderImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeaderImage
        fields = (
            'id',
            'title',
            'image',
        )
