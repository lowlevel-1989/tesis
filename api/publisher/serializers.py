from rest_framework import serializers
from .models import Dewey


class DeweySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dewey