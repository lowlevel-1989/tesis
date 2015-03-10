from rest_framework import viewsets
from rest_framework import filters


from .models      import Brochure
from .serializers import BrochureSerializer


class BrochureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Brochure.objects.all()
    serializer_class    = BrochureSerializer
    filter_backends     = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields       = ('id', 'ubication', 'publisher__name', 'author__name', )
    search_fields       = ('title', 'dewey__description', 'publisher__name', 'isbn', 'ubication', )
