from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^proyectos/nuevo/$', views.new_edit, name='new'),
    url(r'^proyectos/(?P<slug>[-\w]+)/$', views.new_edit, name='edit'),
]
