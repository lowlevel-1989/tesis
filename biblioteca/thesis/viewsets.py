from rest_framework import viewsets
from .models import Thesis
from .serializers import ThesisSerializer


class ThesisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Thesis.objects.all()
    serializer_class    = ThesisSerializer