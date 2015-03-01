from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import PublisherViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'publishers',  PublisherViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

