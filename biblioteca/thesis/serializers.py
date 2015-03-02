from rest_framework import serializers

from author.serializers import AuthorSerializer

from .models import Thesis, Careers


class CareerSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Careers


class ThesisSerializer(serializers.ModelSerializer):

	author = AuthorSerializer(many=True,  read_only=True)
	career = CareerSerializer(many=False, read_only=True)

	is_public = serializers.SerializerMethodField()

	def get_is_public(self, obj):
		if obj.public:
			return obj.thesis_pdf.url
		return None

	class Meta:
	    model  = Thesis
	    fields = ('id', 'title', 'author', 'career', 'year', 'cover', 'abstract_pdf', 'is_public', ) 