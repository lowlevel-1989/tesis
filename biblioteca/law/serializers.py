from rest_framework import serializers

from author.serializers     import AuthorSerializer
from dewey.serializers      import DeweySerializer

from .models import Law


class LawSerializer(serializers.ModelSerializer):
    
    author    = AuthorSerializer    (many=True,  read_only=True)
    dewey     = DeweySerializer     (many=False, read_only=True)

    class Meta:
        model = Law
        fields = ('id', 'title', 'isbn', 'dewey', 'author', 'ubication', 'year', 'cover', ) 
