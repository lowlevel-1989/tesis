from django.contrib import admin
from .models        import Book

class BookAdmin(admin.ModelAdmin):
	list_display      = ('id', 'title', 'dewey', 'publisher', 'isbn', 'year', 'ubication', 'public', 'portada', )
	search_fields     = ('title', 'dewey__description', 'publisher__name', 'isbn', 'ubication')
	list_filter       = ('year', 'ubication', 'publisher__name', 'author__name', )
	raw_id_fields     = ('dewey', 'publisher', )
	filter_horizontal = ('author', )


admin.site.register(Book, BookAdmin)