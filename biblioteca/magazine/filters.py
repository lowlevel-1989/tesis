import operator

from django.db      import models
from django.utils   import six
from rest_framework import filters
from stemming.porter2 import stem

class MagazineFilter(filters.SearchFilter):
   
   def filter_queryset(self, request, queryset, view):
      search_fields = getattr(view, 'search_fields', None)

      if not search_fields:
         return queryset

      searchs = self.get_search_terms(request)
      for index in range(len(searchs)):
         searchs[index] = stem(searchs[index])

      orm_lookups = [self.construct_search(six.text_type(search_field))
                     for search_field in search_fields]

      for search_term in searchs:
         or_queries = [models.Q(**{orm_lookup: search_term})
                        for orm_lookup in orm_lookups]
         queryset = queryset.filter(reduce(operator.or_, or_queries))

      return queryset