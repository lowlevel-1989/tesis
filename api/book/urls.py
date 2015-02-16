from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import DeweyViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'dewey',  DeweyViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

