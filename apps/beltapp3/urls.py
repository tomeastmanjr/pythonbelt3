from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^create$', views.create, name="create"),
    url(r'^show/(?P<item_id>\d+)$', views.show, name="show"),
    url(r'^delete/(?P<item_id>\d+)$', views.delete, name="delete"),
    url(r'^destroy/(?P<item_id>\d+)$', views.destroy, name="destroy"),
    url(r'^update/(?P<item_id>\d+)$', views.update, name="update"),
    url(r'^edit/(?P<item_id>\d+)$', views.edit, name="edit")
    ]
