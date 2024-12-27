from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MovieReview
from .serializers import MovieReviewSerializer
from .permissions import IsReviewerOrReadOnly

class MovieReviewViewSet(viewsets.ModelViewSet):
 
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer
    

  
