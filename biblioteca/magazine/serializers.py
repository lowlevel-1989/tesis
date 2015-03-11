from rest_framework import serializers

from author.serializers     import AuthorSerializer

from .models import Magazine


class MagazineSerializer(serializers.ModelSerializer):
    
    author    = AuthorSerializer    (many=True,  read_only=True)

    class Meta:
        model = Magazine
        fields = ('id', 'title', 'isbn', 'vol', 'author', 'ubication', 'year', 'cover', ) 
