from django.urls import reverse
from rest_framework import status

from blog.models import Blog
from blog.api.serializer import BlogSerializer
from accounts.models import User
from tests.test_config import TestConfig

class BlogListViewTest(TestConfig):

    def test_list_all_blogs(self):
        response = self.client.get(self.blog_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = BlogSerializer([self.sample_blog], many=True).data
        self.assertEqual(response.data, expected_data)

class BlogDetailViewTest(TestConfig):
  
    def test_retrieve_blog_detail(self):
        response = self.client.get(self.blog_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = BlogSerializer(self.sample_blog).data
        self.assertEqual(response.data, expected_data)

    def test_retrieve_nonexistent_blog(self):
        invalid_url = reverse('blog-detail', args=[99999])  
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class BlogCreateViewTest(TestConfig):
 
    def test_create_blog_unauthorized_user(self):
        response = self.client.post(
            self.blog_create_url, 
            BlogSerializer(self.sample_blog).data, 
        )
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_blog_authorized_user(self):
        response = self.client.post(
            self.blog_create_url, 
            BlogSerializer(self.sample_blog).data, 
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        expected_data = BlogSerializer(Blog.objects.all().first()).data
        self.assertEqual(response.data, expected_data)


    def test_invalid_blog_data(self):
      
        blog = {
            'title': '', 
            'content': 'Test Content',
        }
        response = self.client.post(
            self.blog_create_url, 
            BlogSerializer(blog).data, 
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )       

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class BlogUpdateDeleteViewTest(TestConfig):
    def test_update_blog(self):
        data = {
            'title': 'Updated Blog',
            'content': 'Updated Content',
        }

        response = self.client.put(
            self.blog_update_url, 
            data, 
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_blog = Blog.objects.get(pk=self.sample_blog.id)

        self.assertEqual(updated_blog.title, 'Updated Blog')
        self.assertEqual(updated_blog.content, 'Updated Content')

    def test_delete_blog(self):
        response = self.client.delete(
            self.blog_delete_url,
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Blog.objects.filter(pk=self.sample_blog.pk).exists())

    def test_update_blog_unauthorized(self):
  
        data = {
            'title': 'Updated Blog',
            'content': 'Updated Content',
        }

        response = self.client.put(self.blog_update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_blog_unauthorized(self):
        response = self.client.delete(self.blog_delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

