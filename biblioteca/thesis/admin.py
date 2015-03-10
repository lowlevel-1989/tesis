from django.contrib import admin
from .models        import Careers, Thesis, Line

class CareersAdmin(admin.ModelAdmin):
	list_display  = ('name', )
	search_fields = ('name', )


class LineAdmin(admin.ModelAdmin):
	list_display  = ('name', )
	search_fields = ('name', )


class ThesisAdmin(admin.ModelAdmin):
	list_display      = ('title', 'line', 'year', 'public', 'portada', )
	search_fields     = ('title', 'career__name', 'author__name', 'line__name', )
	list_filter       = ('career__name', 'author__name', 'line__name', 'year', )
	filter_horizontal = ('author', )


admin.site.register(Careers, CareersAdmin)
admin.site.register(Line,    LineAdmin   )
admin.site.register(Thesis,  ThesisAdmin )