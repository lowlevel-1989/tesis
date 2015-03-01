from rest_framework import serializers
from .models import Thesis


class ThesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thesis