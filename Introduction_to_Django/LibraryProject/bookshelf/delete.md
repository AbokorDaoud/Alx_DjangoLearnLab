

from bookshelf.models import Book

# Delete Operation

```python
# Delete the book instance
book.delete()
Book.objects.all()  # Expected output: <QuerySet []>
