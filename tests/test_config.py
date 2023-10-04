from django.urls import reverse

from rest_framework.test import APITestCase

from accounts.models import User
from blog.models import Blog

class TestConfig(APITestCase):

    def setUp(self):

        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.blog_list_url = reverse('blog-list')  
        self.blog_create_url = reverse('blog-create')  


        self.user_data = {
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password': 'mypassword',
        }

        self.user = User.objects.create_user(**self.user_data)
        self.sample_blog = Blog.objects.create(title='Blog 1', content='Content 1', author=self.user)
        self.blog_detail_url = reverse('blog-detail', args=[self.sample_blog.id])
        self.blog_update_url = reverse('blog-update', args=[self.sample_blog.id])
        self.blog_delete_url = reverse('blog-delete', args=[self.sample_blog.id])
        self.token = self.authenticate_user()

        return super().setUp()
    
    def authenticate_user(self):
        auth_reponse = self.client.post(
            self.login_url,
            self.user_data, 
            format="json"
        )
        token = auth_reponse.data['token'].decode('utf-8')
        return token

    
    def tearDown(self):
        return super().tearDown()