from rest_framework import viewsets
from rest_framework import filters


from .models      import Magazine
from .filters     import MagazineFilter
from .serializers import MagazineSerializer


class MagazineViewSet(viewsets.ReadOnlyModelViewSet):
   queryset            = Magazine.objects.all()
   serializer_class    = MagazineSerializer
   filter_backends     = (filters.DjangoFilterBackend, MagazineFilter, )
   filter_fields       = ('id', 'year', 'ubication', 'author__name', )
   search_fields       = ('title', 'isbn', )
