from django.db import models
from miniblog.article.models import Article, Author


class Comment(models.Model):
    body = models.TextField()
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.id}: {self.body[:10]}..."
