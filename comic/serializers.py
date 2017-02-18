from rest_framework import serializers

from .models import *


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = (
            'id',
            'name',
            'image',
            'description',
            'comics',
        )

class ComicSerializer(serializers.ModelSerializer):
    cast_members = CastSerializer(many=True, read_only=True)

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

class IssueSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Issue
        fields = (
            'id',
            'title',
            'image',
            'issue_number',
        )

class HeaderImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderImage
        fields = (
            'id',
            'title',
            'image',
        )
