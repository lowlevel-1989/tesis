from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import ThesisViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'thesis',  ThesisViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

