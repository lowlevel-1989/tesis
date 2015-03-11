from django.contrib import admin
from .models        import Magazine


class MagazineAdmin(admin.ModelAdmin):
	list_display      = ('id', 'title', 'isbn', 'year', 'ubication', 'portada', )
	search_fields     = ('title', 'isbn', 'ubication')
	list_filter       = ('year', 'ubication', 'author__name', )
	filter_horizontal = ('author', )

admin.site.register(Magazine, MagazineAdmin)