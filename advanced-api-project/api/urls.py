from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

# Initialize the DefaultRouter for automatic URL routing of ViewSets
router = DefaultRouter()
# Register the BookViewSet with the router under the 'books' prefix
router.register(r'books', BookViewSet)

# Define urlpatterns for class-based views
urlpatterns = [
    # URL pattern for listing all books
    path('api/books/', BookListView.as_view(), name='book-list'),
    # URL pattern for retrieving details of a specific book by its primary key
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    # URL pattern for creating a new book
    path('api/books/create/', BookCreateView.as_view(), name='book-create'),
    # URL pattern for updating an existing book
    path('books/update', BookUpdateView.as_view(), name='book-update'),
    # URL pattern for deleting a book
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),
]

# Include the router-generated URL patterns
urlpatterns += router.urls
