import unittest
from app.models import *
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(id = 12345,username='cha', password='chako', email='test@test.com')
        self.new_blog = Blog(id=1, title='Test', description='ha ha', blog='This is a test blog', user_id=12345)

    def tearDown(self):
        Blog.query.delete_blog()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.description, 'ha ha')
        self.assertEquals(self.new_blog.blog, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, 12345)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)