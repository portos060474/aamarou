from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views
from django.conf.urls import include, url
from django.contrib import admin



urlpatterns =[
    url(r'^$', views.home, ),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name':'accounts/logout.html'}),


]





