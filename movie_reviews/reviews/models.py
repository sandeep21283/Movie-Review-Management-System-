from django.db import models
from django.contrib.auth.models import User

class MovieReview(models.Model):
   
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie_title = models.CharField(max_length=255)
    review_text = models.TextField()
  
    

    def __str__(self):
        return f"{self.movie_title} - {self.reviewer.username}"
