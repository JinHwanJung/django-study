from rest_framework.viewsets import ReadOnlyModelViewSet

from test_app.user.models import User
from test_app.user.serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
