from rest_framework import serializers
from .models import BookCategory, Books, BookStatus, BookVendor, CupBoard, CupBoardShelf, IssueBook, Fine, CupboardShelfField

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class BooksSerializer(serializers.ModelSerializer):
    # is_available = serializers.ReadOnlyField()
    class Meta:
        model = Books
        fields = "__all__"

class BookStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatus
        fields = "__all__"


class BookVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookVendor
        fields = "__all__"

class CupboardShelfFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = CupboardShelfField
        fields = "__all__"

class CupBoardSerializer(serializers.ModelSerializer):
    cupboardfields = CupboardShelfFieldSerializer(many=True, read_only=True)
    class Meta:
        model = CupBoard
        fields = "__all__"


class CupBoardShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = CupBoardShelf
        fields = "__all__"


class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = "__all__"
  

class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = "__all__"


