from django.core.management.base import BaseCommand
import requests
import json


class Command(BaseCommand):
    help = "Consume the user registration API"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('email', type=str, help='Email address')
        parser.add_argument('password', type=str, help='Password')
        

    def handle(self, *args, **kwargs):
        api_url = 'http://127.0.0.1:8000/api/auth/register/'
        headers={'Content-Type': 'application/json'}
        data = {
            "username":kwargs['username'],
            "email":kwargs['email'],
            "password":kwargs['password']
        }

        response = requests.post(api_url, json.dumps(data), headers=headers)

        if response.status_code == 201:
            api_data = response.json()
            token = api_data['token']
            self.stdout.write(self.style.SUCCESS(f'Successfully Registered: token -> {token}'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to consume API: {response.json()}'))
            