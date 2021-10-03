from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ArticleViewSet, CommentViewSet


router = DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)

urlpatterns = [
    path('users/<int:user_id>/articles', ArticleViewSet.as_view({'get': 'list'})),
    path('users/<int:user_id>/articles/<int:article_id>', ArticleViewSet.as_view({'get': 'retrieve'}, lookup_url_kwarg='article_id')),
    path('users/<int:user_id>/articles/<int:article_id>/comments', CommentViewSet.as_view({'get': 'list'})),
    path('users/<int:user_id>/articles/<int:article_id>/comments/<int:comment_id>', CommentViewSet.as_view({'get': 'retrieve'}, lookup_url_kwarg='comment_id')),
    path('', include(router.urls)),
]
