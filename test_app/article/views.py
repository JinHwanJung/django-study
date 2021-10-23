from rest_framework.viewsets import ReadOnlyModelViewSet
from article.models import Article
from article.serializers import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
