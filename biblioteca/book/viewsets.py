from rest_framework import viewsets
from rest_framework import filters


from .models      import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Book.objects.all()
    serializer_class    = BookSerializer
    filter_backends     = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields       = ('id', 'title', 'author__name', 'publisher__name', 'year', 'publisher__country', )
    search_fields       = ('title', 'dewey__description', 'publisher__name', 'isbn', 'author__name', )
