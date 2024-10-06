import requests
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        api_key = '51994fc2e7969ea0e9a79d6a0f95fa63' ##tmdb API key
        language = 'tr-TR'
        base_url = 'https://api.themoviedb.org/3/movie/popular'
        page = 1

        while True:
            url = f'{base_url}?api_key={api_key}&language={language}&page={page}'
            response = requests.get(url)
            data = response.json()

            if 'results' not in data or not data['results']:
                break

            for item in data['results']:
                release_date = item.get('release_date') or None
                if release_date == '':
                    release_date = None

                movie, created = Movie.objects.update_or_create(
                    tmdb_id=item['id'],
                    defaults={
                        'title': item['title'],
                        'overview': item['overview'],
                        'release_date': release_date,
                        'poster_path': f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item['poster_path'] else None,
                        'language': language,
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added movie: {movie.title}"))
                else:   
                    self.stdout.write(self.style.WARNING(f"Updated movie: {movie.title}"))

            if page >= data.get('total_pages', 1):
                break

            page += 1
