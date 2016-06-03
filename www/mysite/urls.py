"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

from rest_framework import routers
from api import views as api_views

class CrmsStaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'profiles', api_views.ProfileViewSet)
router.register(r'cars', api_views.CarViewSet)
router.register(r'offers', api_views.OfferViewSet)
router.register(r'deals', api_views.DealViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^(?P<template_name>\w+)$', CrmsStaticView.as_view()),
]
