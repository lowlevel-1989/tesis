from rest_framework import viewsets
from rest_framework import filters


from .models      import Law
from .serializers import LawSerializer


class LawViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Law.objects.all()
    serializer_class    = LawSerializer
    filter_backends     = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields       = ('id', 'year', 'ubication', 'author__name', )
    search_fields       = ('title', 'dewey__description', 'isbn')
