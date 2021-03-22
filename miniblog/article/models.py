from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='article', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.id}: {self.body[:10]}..."
