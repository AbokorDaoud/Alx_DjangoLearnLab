from django.db import models
from django.contrib.auth.models import User

# Define the Author model to store information about book authors.
class Author(models.Model):
    # The author's first name, stored as a character field with a maximum length of 20 characters.
    first_name = models.CharField(max_length=20)
    # The author's last name, stored as a character field with a maximum length of 20 characters.
    last_name = models.CharField(max_length=20)

    # String representation of the Author object, returning the full name.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the Book model to store information about books.
class Book(models.Model):
    # The title of the book, stored as a character field with a maximum length of 50 characters.
    title = models.CharField(max_length=50)
    # The year the book was published, stored as a small integer field.
    publication_year = models.SmallIntegerField()
    # ForeignKey to the Author model, establishing a many-to-one relationship.
    # If the referenced Author is deleted, all related Book instances will also be deleted (CASCADE).
    # The related_name 'books' allows access to a list of books for a given author (e.g., author.books.all()).
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # ForeignKey to the User model, indicating which user added the book.
    # If the referenced User is deleted, all related Book instances will also be deleted (CASCADE).
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # String representation of the Book object, including its title, publication year, and author.
    def __str__(self):
        return f"{self.title} published in the year {self.publication_year} by {self.author}"

    # Meta class to define additional model options.
    class Meta:
        # Custom permissions for the Book model.
        # Each tuple consists of a permission codename and a human-readable name.
        permissions = [
            ("CreateView", "Can Create"),  # Permission to create a book.
            ("UpdateView", "Can Update"),  # Permission to update a book.
            ("DeleteView", "Can Delete"),  # Permission to delete a book.
        ]
