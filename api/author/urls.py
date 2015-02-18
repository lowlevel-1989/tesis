from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import AuthorViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'authors',  AuthorViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

