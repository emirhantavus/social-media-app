from django.db import models

class Movie(models.Model):
      tmdb_id = models.IntegerField(unique=True)
      title = models.CharField(max_length=255)
      overview = models.TextField()
      release_date = models.DateField(null=True, blank=True)
      poster_path = models.URLField(null=True, blank=True)
      language = models.CharField(max_length=10, default='tr-TR')
      created_at = models.DateTimeField(auto_now_add=True)  
      
      def __str__(self):
            return self.title   ### TMDB datas are used here
