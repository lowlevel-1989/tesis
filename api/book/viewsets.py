from rest_framework import viewsets
from .models import Dewey
from .serializers import DeweySerializer


class DeweyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Dewey.objects.all()
    serializer_class    = DeweySerializer