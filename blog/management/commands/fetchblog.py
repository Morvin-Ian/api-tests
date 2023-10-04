from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = "Consume the Fetch Single Blog API"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='The pk of the blog')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        api_url = f"http://127.0.0.1:8000/api/blogs/{id}/"
  
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()
            self.stdout.write(self.style.SUCCESS(f'Blog {id}: {api_data}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to consume API: {response.json()}'))
            