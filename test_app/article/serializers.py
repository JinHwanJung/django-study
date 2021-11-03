from rest_framework.serializers import ModelSerializer

from test_app.article.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
