from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls  )),
    url(r'^',   include('author.urls'        )),
    url(r'^',   include('dewey.urls'         )),
    url(r'^',   include('book.urls'          )),
    url(r'^',   include('publisher.urls'     )),
    url(r'^',   include('thesis.urls'        )),
    url(r'^',   include('brochure.urls'      )),
    url(r'^',   include('law.urls'           )),
)

if settings.DEBUG:
	urlpatterns += patterns('',
	    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
	)