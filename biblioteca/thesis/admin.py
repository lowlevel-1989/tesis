from django.contrib import admin
from .models        import Careers, Thesis

class CareersAdmin(admin.ModelAdmin):
	list_display  = ('name', )
	search_fields = ('name', )


class ThesisAdmin(admin.ModelAdmin):
	list_display      = ('title', 'career', 'year', 'public', 'portada', )
	search_fields     = ('title', 'career', )
	list_filter       = ('career', 'year', 'author__name', )
	filter_horizontal = ('author', )


admin.site.register(Careers, CareersAdmin)
admin.site.register(Thesis, ThesisAdmin)