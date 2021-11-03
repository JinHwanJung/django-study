from rest_framework.viewsets import ReadOnlyModelViewSet
from test_app.article.models import Article
from test_app.article.serializers import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
