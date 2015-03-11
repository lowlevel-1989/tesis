from rest_framework import viewsets
from rest_framework import filters


from .models      import Magazine
from .serializers import MagazineSerializer


class MagazineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Magazine.objects.all()
    serializer_class    = MagazineSerializer
    filter_backends     = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields       = ('id', 'year', 'ubication', 'author__name', )
    search_fields       = ('title', 'isbn', )
