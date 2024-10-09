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
      
      
class Genre(models.Model):
      GENRE_CHOICES = [
            ('macera', 'Macera'),
            ('korku', 'Korku'),
            ('komedi', 'Komedi'),
            ('dram', 'Dram'),
            ('fantastik', 'Fantastik'),
            ('gerilim', 'Gerilim'),
            ('romantik', 'Romantik'),
            ('aksiyon', 'Aksiyon'),
            ('bilimkurgu', 'Bilim Kurgu'),
            ('gizem', 'Gizem'),
            ('belgesel', 'Belgesel'),
            ('biyografi', 'Biyografi'),
            ('suç', 'Suç'),
            ('savaş', 'Savaş'),
            ('tarih', 'Tarih'),
            ('müzikal', 'Müzikal'),
            ('psikolojik', 'Psikolojik'),
            ('spor', 'Spor'),
            ('western', 'Western'),
            ('animasyon', 'Animasyon'),
            ('çocuk', 'Çocuk'),
            ('kısa', 'Kısa Film'),
            ('sanat', 'Sanat'),
            ('distopya', 'Distopya'),
      ]
    
      name = models.CharField(max_length=50, choices=GENRE_CHOICES, unique=True)

      def __str__(self):
            return dict(self.GENRE_CHOICES).get(self.name)