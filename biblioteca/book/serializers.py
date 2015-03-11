from rest_framework import serializers

from author.serializers     import AuthorSerializer
from dewey.serializers      import DeweySerializer
from publisher.serializers  import PublisherSerializer

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    
    author    = AuthorSerializer    (many=True,  read_only=True)
    dewey     = DeweySerializer     (many=False, read_only=True)
    publisher = PublisherSerializer (many=False, read_only=True)

    is_public = serializers.SerializerMethodField()

    def get_is_public(self, obj):
        if obj.public:
            return obj.book_pdf.url
        return None

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'dewey', 'author', 'publisher', 'ubication', 'pages', 'year', 'cover', 'is_public', ) 
