from django.db import models

class Category(models.Model):
      CATEGORY_CHOICES = [
            ('movie', 'Movie'),
            ('series', 'Series'),
            ('book', 'Book'),
            ('anime', 'Anime'),
      ]

      name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

      def __str__(self):
            return self.get_name_display()