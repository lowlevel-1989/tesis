from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import UserViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'users',  UserViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

