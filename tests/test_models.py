from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings


from datetime import datetime, timedelta
import jwt

from accounts.models import User
from blog.models import Blog



User = get_user_model()

class TestUserModel(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@gmail.com',
            'password': 'mypassword',
        }

    def test_create_user(self):
        user = User.objects.create_user(**self.user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.user_data['email'])
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        user = User.objects.create_superuser(**self.user_data)
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.username, self.user_data['username'])

    def test_superuser_is_staff_status_value_error(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(**self.user_data, is_staff=False)

    def test_superuser_is_superuser_status_value_error(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(**self.user_data, is_superuser=False)

    def test_username_value_error(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='test@gmail.com', password="mypass")
        self.assertRaisesMessage(ValueError,"The given username must be set")

    def test_email_value_error(self):
        self.assertRaises(ValueError, User.objects.create_user, username="testuser", email="", password="mypass")
        self.assertRaisesMessage(ValueError,"The given email must be set")


    def test_token_generation(self):
        user = User(**self.user_data)
        token = user.token

        test_payload = {
            'username': self.user_data['username'],
            'email': self.user_data['email'],
            'exp': datetime.utcnow() + timedelta(hours=1),
        }

        test_token = jwt.encode(test_payload, settings.SECRET_KEY, algorithm='HS256')
        self.assertEqual(token, test_token)

    def test_str(self):
        user = User.objects.create_user(**self.user_data)
        self.assertEqual(str(user), self.user_data['email'])


class BlogModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='mypassword'
        )

        self.blog = Blog.objects.create(
            title='Test Blog',
            content='This is a test blog content.',
            author=self.user
        )

    def test_blog_model_creation(self):
        self.assertEqual(self.blog.title, 'Test Blog')
        self.assertEqual(self.blog.content, 'This is a test blog content.')
        self.assertEqual(self.blog.author, self.user)

    def test_blog_model_str_method(self):
        self.assertEqual(str(self.blog), 'Test Blog')


    def test_verbose_names(self):
        self.assertEqual(Blog._meta.verbose_name, 'Blog')
        self.assertEqual(Blog._meta.verbose_name_plural, 'Blogs')
