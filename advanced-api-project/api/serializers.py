from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # Specify the fields to be included in the serialized output
        fields = ['id', 'title', 'author', 'publication_year']

    # Custom validator for the publication_year field
    def validate_publication_year(self, value):
        current_year = date.today().year
        # Ensure the publication year is not in the future
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include related books in the author representation
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # Include all fields from the Author model
        fields = '__all__'
