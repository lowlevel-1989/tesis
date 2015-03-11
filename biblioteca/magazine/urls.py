from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import MagazineViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'magazines',  MagazineViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

