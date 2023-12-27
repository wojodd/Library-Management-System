from rest_framework import serializers
from .models import Author, Publisher, Langauge, Category, Section, Faculty, Book, Copy, Ebook, New, Library

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"

class LangaugeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langauge
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = "__all__"

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = "__all__"

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"