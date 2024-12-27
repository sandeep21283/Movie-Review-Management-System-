from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieReviewViewSet

router = DefaultRouter()
router.register(r'moviereviews', MovieReviewViewSet, basename='moviereview')

urlpatterns = [
    path('', include(router.urls)),  # This will generate all CRUD routes
]
