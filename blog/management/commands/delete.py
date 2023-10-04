from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = "Consume the Fetch Single Blog API"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='The pk of the blog')
        parser.add_argument('token', type=str, help='Auth Token')

    
    def handle(self, *args, **kwargs):
        id = kwargs['id']
        token = kwargs['token']
        api_url = f"http://127.0.0.1:8000/api/blogs/{id}/delete/"

        headers = {
            'Authorization': f'Bearer {token}',
        }

  
        response = requests.delete(
            api_url,
            headers=headers
        )

        if response.status_code == 204:
            self.stdout.write(self.style.SUCCESS(f'Successfully Deleted the Blog: {response}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to consume API: {response.json()}'))
            