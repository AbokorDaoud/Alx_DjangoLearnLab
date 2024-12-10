from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

app_name = 'posts'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# The following URL patterns are actually automatically created by the router due to @action decorators
# but we're making them explicit here for clarity
urlpatterns = [
    path('', include(router.urls)),
    path('feed/', PostViewSet.as_view({'get': 'feed'}), name='post-feed'),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
]
