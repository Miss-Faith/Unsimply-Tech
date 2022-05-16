import unittest
from app.models import *
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_James = User(id = 12345, username = 'James', email = 'james@ms.com')
        self.new_comment = Comment(comment='This blog is the best thing since sliced bread',user_id = self.user_James,blog_id=123)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'This blog is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user_id,self.user_James)
        self.assertEquals(self.new_comment.blog_id,123)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)