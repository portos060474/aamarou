
from django.conf.urls import url
from naissance import views

app_name = 'naissance'

urlpatterns = [
    url(r'^$', views.rnaissance),
    url(r'^acten/(.{1,9})-(.{1,9})/$', views.get_actenaissance, name='detail'),
    url(r'^acten/(.{1,9})-(.{1,9})/$', views.get_actenaissance, name='get_actenaissance'),
    url(r'^naissance/(.{1,9})/$', views.anaissance),
    url(r'^acten/(.{1,9})-(.{1,9})/confirm$', views.confirm, name='confirm'),
   ]