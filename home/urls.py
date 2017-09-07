from django.conf.urls import url

from . import home

urlpatterns = [
    url(r'^$', views.index, name='index'),
]