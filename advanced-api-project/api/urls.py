from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/books/', BookListView.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update', BookUpdateView.as_view(), name='book-update'),
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),
]

