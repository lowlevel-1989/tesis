from django.contrib import admin
from .models        import Law

class LawAdmin(admin.ModelAdmin):
	list_display      = ('id', 'title', 'dewey', 'isbn', 'year', 'ubication', 'portada', )
	search_fields     = ('title', 'dewey__description', 'isbn', 'ubication')
	list_filter       = ('year', 'ubication', 'author__name', )
	raw_id_fields     = ('dewey', )
	filter_horizontal = ('author', )


admin.site.register(Law, LawAdmin)