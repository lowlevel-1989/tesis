from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import LawViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'laws',  LawViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

