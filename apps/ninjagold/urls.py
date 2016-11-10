from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_gold/(?P<location>[a-z]*)$', views.gold)
]
