from django.contrib import admin
from .models        import Publisher

class PublisherAdmin(admin.ModelAdmin):
	list_display  = ('name', 'country', 'state', 'city', )
	search_fields = ('name', 'country', 'state', 'city', )

admin.site.register(Publisher, PublisherAdmin)
