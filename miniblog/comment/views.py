from rest_framework import viewsets

from .models import Comment
from .serializers import CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
