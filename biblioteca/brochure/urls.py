from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import BookViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'books',  BookViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

