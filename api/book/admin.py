from django.contrib import admin
from .models        import Book

class BookAdmin(admin.ModelAdmin):
	list_display      = ('title', 'dewey', 'publisher', 'isbn', 'year', 'pais', 'public', 'portada', )
	search_fields     = ('title', 'dewey__description', 'publisher__name', 'isbn', )
	list_filter       = ('year', 'publisher__country', 'publisher__name', 'author__name', )
	raw_id_fields     = ('dewey', 'publisher', )
	filter_horizontal = ('author', )


admin.site.register(Book, BookAdmin)