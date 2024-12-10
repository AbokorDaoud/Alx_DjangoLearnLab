from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from rest_framework import status

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        # Check if user already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response(
                {'error': 'You have already liked this post.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create like
        like = Like.objects.create(user=user, post=post)
        
        # Create notification for post author
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='like',
                content_type=ContentType.objects.get_for_model(post),
                object_id=post.id
            )
        
        return Response(
            LikeSerializer(like).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        like = get_object_or_404(Like, user=user, post=post)
        like.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def feed(self, request):
        """
        Returns a feed of posts from users that the current user follows,
        ordered by creation date (newest first).
        """
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['post']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        
        # Create notification for post author when someone comments
        if comment.post.author != self.request.user:
            Notification.objects.create(
                recipient=comment.post.author,
                actor=self.request.user,
                verb='comment',
                content_type=ContentType.objects.get_for_model(comment.post),
                object_id=comment.post.id
            )
