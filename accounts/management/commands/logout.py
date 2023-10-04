from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = "Consume the user Logout API"

    def add_arguments(self, parser):
        parser.add_argument('token', type=str, help='Auth token')
        

    def handle(self, *args, **kwargs):
        api_url = 'http://127.0.0.1:8000/api/auth/logout/'
        token = kwargs['token']

        response = requests.get(api_url,  
            headers = {
            'Authorization': f'Bearer {token}',
        })

        if response.status_code == 204:
            self.stdout.write(self.style.SUCCESS(f'Successfully consumed API data: Status Code -  {response.status_code}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to consume API: Status Code - {response.status_code}'))
            