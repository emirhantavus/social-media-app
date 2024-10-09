from django.db import models

class Category(models.Model):
      CATEGORY_CHOICES = [
            ('film', 'Film'),
            ('dizi', 'Dizi'),
            ('kitap', 'Kitap'),
            ('anime', 'Anime'),
      ]

      name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

      def __str__(self):
            return self.get_name_display()