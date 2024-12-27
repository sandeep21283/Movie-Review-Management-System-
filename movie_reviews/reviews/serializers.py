from rest_framework import serializers
from .models import MovieReview

class MovieReviewSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = MovieReview
        fields = [
            'id',
            'reviewer',
            'movie_title',
            'review_text',
            'rating',
            'created_at',
            'updated_at',
        ]
