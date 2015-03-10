from rest_framework import serializers

from author.serializers     import AuthorSerializer
from publisher.serializers  import PublisherSerializer


from .models import Brochure


class BrochureSerializer(serializers.ModelSerializer):
    
    author    = AuthorSerializer    (many=True,  read_only=True)
    publisher = PublisherSerializer (many=False, read_only=True)

    class Meta:
        model = Brochure
        fields = ('id', 'title', 'publisher', 'isbn', 'author', 'ubication', 'year', 'cover', ) 
