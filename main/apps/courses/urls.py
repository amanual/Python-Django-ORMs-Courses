from django.conf.urls import url 
from . import views

urlpatterns= [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^caution/(?P<id>\d+)$', views.caution),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),

]