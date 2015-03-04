from rest_framework import serializers

from author.serializers     import AuthorSerializer
from dewey.serializers      import DeweySerializer
from publisher.serializers  import PublisherSerializer

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    
    author    = AuthorSerializer    (many=True,  read_only=True)
    dewey     = DeweySerializer     (many=False, read_only=True)
    publisher = PublisherSerializer (many=False, read_only=True)

    class Meta:
        model = Book