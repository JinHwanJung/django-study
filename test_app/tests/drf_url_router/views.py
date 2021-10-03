from rest_framework.viewsets import ModelViewSet
from .models import Article, Comment
from .serializers import UserSerializer, ArticleSerializer, CommentSerializer
from user.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = self.queryset
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs.get('article_id')
        queryset = self.queryset
        if article_id:
            queryset = queryset.filter(article_id=article_id)
        return queryset
