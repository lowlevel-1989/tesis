from django.contrib import admin
from .models        import Brochure

class BrochureAdmin(admin.ModelAdmin):
	list_display      = ('title', 'publisher', 'isbn', 'year', 'ubication', 'portada', )
	search_fields     = ('title', 'publisher__name', 'isbn', 'ubication', )
	list_filter       = ('year', 'ubication', 'publisher__name', 'author__name', )
	raw_id_fields     = ('publisher', )
	filter_horizontal = ('author', )


admin.site.register(Brochure, BrochureAdmin)