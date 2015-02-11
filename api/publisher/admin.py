from django.contrib import admin
from .models import Publisher

class PublisherAdmin (admin.ModelAdmin):
	list_display  = ('name', 'city', 'state', 'country', )
	search_fields = ('name', 'city', 'state', 'country', )

admin.site.register(Publisher)
