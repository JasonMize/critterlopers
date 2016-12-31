from rest_framework import serializers

from .models import *


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = (
            'id',
            'page_number',
            'title',
            'issue',
            'image',
            'date_added',
            'cast_members',
        )

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = (
            'id',
            'name',
            'image',
            'comics',
        )


class HeaderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderImage
        fields = (
            'id',
            'title',
            'image',
        )
