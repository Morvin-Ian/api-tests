from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = "Consume the Fetch All Blogs API"

    def handle(self, *args, **kwargs):
        api_url = 'http://127.0.0.1:8000/api/blogs/'
  
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()
            self.stdout.write(self.style.SUCCESS(f'Blogs: {api_data}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to consume API: {response.json()}'))
            