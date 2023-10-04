from django.test import TestCase
from accounts.models import User
from blog.models import Blog


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
