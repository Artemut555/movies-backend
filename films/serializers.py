from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        ordering = ['-id']
        fields = ('pk', 'imdbId', 'Title', 'Poster', 'Rating')
