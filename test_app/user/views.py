from rest_framework.viewsets import ReadOnlyModelViewSet

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
