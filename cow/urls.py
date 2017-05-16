"""cow URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from nutrition import views as nutrition_views
from django.conf import settings

urlpatterns = [
    url(r'^$', nutrition_views.home, name='home'),
    url(r'^news/', nutrition_views.news, name='news'),
    url(r'^cal/', nutrition_views.cal, name='cal'),
    url(r'^fodder/', nutrition_views.fodder, name='fodder'),
    url(r'^dataIn/', nutrition_views.dataIn, name='dataIn'),
    url(r'^dataOut/', nutrition_views.dataOut, name='dataOut'),
    url(r'^info/', nutrition_views.info, name='info'),
    url(r'^dmi/', nutrition_views.dmi, name='dmi'),
    url(r'^fcm/', nutrition_views.fcm, name='fcm'),
    url(r'^de1x/', nutrition_views.de1x, name='de1x'),
    url(r'^tdn/', nutrition_views.tdn, name='tdn'),
    url(r'^tdnpre/', nutrition_views.tdnpre, name='tdnpre'),
    url(r'^ne/', nutrition_views.ne, name='ne'),
    url(r'^nfc/', nutrition_views.nfc, name='nfc'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
