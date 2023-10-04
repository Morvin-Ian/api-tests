from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import User
from tests.test_config import TestConfig


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register') 

        self.data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }

    def test_sucessful_registration(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertTrue(User.objects.filter(email=self.data['email']).exists())
    
    def test_no_body_registration(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(User.objects.filter(email=self.data['email']).exists())



class LoginViewTest(TestConfig):
    def test_sucessful_login(self):
        reponse = self.client.post(
            self.login_url,
            self.user_data, 
            format="json"
        )
        self.assertEqual(reponse.status_code, 200)
        self.assertTrue(User.objects.filter(email=self.user_data['email']).exists())


    def test_no_body_login(self):
        reponse = self.client.post(self.login_url)
        self.assertEqual(reponse.status_code, 401)


class LogoutViewTest(TestConfig):
    
    def test_logout(self):
        logout_response = "Logged out successfully"
   
        response = self.client.get(
            self.logout_url,
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, logout_response)

        



