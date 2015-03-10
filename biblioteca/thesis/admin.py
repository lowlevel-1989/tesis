from django.contrib import admin
from .models        import Careers, Thesis

class CareersAdmin(admin.ModelAdmin):
	list_display  = ('name', )
	search_fields = ('name', )


class ThesisAdmin(admin.ModelAdmin):
	list_display      = ('title', 'career', 'line', 'year', 'public', 'portada', )
	search_fields     = ('title', 'career', 'line', )
	list_filter       = ('career', 'year', 'author__name', 'line', )
	filter_horizontal = ('author', )


admin.site.register(Careers, CareersAdmin)
admin.site.register(Thesis, ThesisAdmin)