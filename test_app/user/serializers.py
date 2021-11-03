from rest_framework.serializers import ModelSerializer

from test_app.user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)
