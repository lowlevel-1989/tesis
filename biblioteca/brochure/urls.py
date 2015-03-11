from django.conf.urls import patterns, url, include
from rest_framework.routers import SimpleRouter

from .viewsets import BrochureViewSet

simpleRouter = SimpleRouter()
simpleRouter.register(r'brochures',  BrochureViewSet)
routerUrls = simpleRouter.urls

urlpatterns = patterns('.viewsets',
    url(r'^', include(routerUrls)),
)

