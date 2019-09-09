from datetime import datetime

from rest_framework.test import APITestCase
# Create your tests here.

from .models import Post, Author
from .api import PostSerializer


class GetPostsTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # cls._test_data = object()
        a1 = Author.objects.create(name="Ivan")
        a2 = Author.objects.create(name="John")
        cls.authors = [a1, a2]
        cls.posts = [
            Post.objects.create(title="A", content="ABC", author=a1, created_at=datetime(2020, 10, 20)),
            Post.objects.create(title="B", content="ABC", author=a1, created_at=datetime(2020, 10, 21)),
            Post.objects.create(title="C", content="ABC", author=a2, created_at=datetime(2020, 10, 22)),
            Post.objects.create(title="D", content="ABC", author=a2, created_at=datetime(2020, 11, 20)),
            Post.objects.create(title="E", content="ABC", author=a2, created_at=datetime(2020, 6, 20))
        ]

    def test_filter_by_date(self):
        r = self.client.get('/api/posts/', data={"date_from": "2020-10-20",
                                                 "date_to": "2020-10-27"})
        self.assertEqual(list(map(lambda x: x["title"], r.data)), ['C', 'B', 'A'])

    def test_format_annotation(self):
        # short
        p = Post(title="A", content="ABC", author=self.authors[0], created_at=datetime(2020, 10, 20))
        a = PostSerializer.get_annotation(p)
        self.assertEqual(a, "ABC")

        # long (140)
        p.content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque interdum" \
                    " rutrum sodales. Nullam mattis fermentum libero, non volutpat."
        a = PostSerializer.get_annotation(p)
        self.assertTrue(len(a) <= 100)
        content_words = set(p.content.split(" "))
        a_words = set(a.split(" "))
        self.assertTrue(a_words <= content_words)
