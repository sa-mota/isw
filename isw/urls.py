"""isw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

import coordination.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^isw/calls/logo/$', TemplateView.as_view(template_name='isw/calls/logo.html'), name='isw-calls-logo'),

    url(r'^sicpe/delete/generation/(?P<pk>\d+)/$', coordination.views.DeleteGenerationView.as_view(), name='generations-delete'),

    url(r'^sicpe/detail/generation/(?P<pk>\d+)/$', coordination.views.GenerationView.as_view(), name='generations-view',),

    url(r'^sicpe/new/generation/$', coordination.views.CreateGenerationView.as_view(), name='generations-new',),

    url(r'^sicpe/list/generation/$', coordination.views.ListGenerationView.as_view(), name='generations-list',),

    url(r'^sicpe/edit/generation/(?P<pk>\d+)/$', coordination.views.UpdateGenerationView.as_view(), name='generations-edit',),
]
