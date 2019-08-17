"""blog URL Configuration

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
from blogapp.views import IndexView,AritcleDetail,AllAritcleView,AboutView,ContactView,PaginatorView,All_Sort_AritcleView
from blogapp.views import All_Tage_AritcleView,AritcleComment,LoginView,RegisiteView,LoginOutView,UserInfoView
urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^index_page/(?P<page_id>\d+)$',PaginatorView.as_view(),name='index_list'),
    url(r'^all/(?P<page_id>\d+)$',AllAritcleView.as_view(),name='all'),
    url(r'^detail/(?P<article_id>\d+)$',AritcleDetail.as_view(),name='detail'),
    url(r'^about$',AboutView.as_view(),name='about'),
    url(r'^contact$',ContactView.as_view(),name='contact'),
    url(r'^sort/(?P<page_id>\d+)$',All_Sort_AritcleView.as_view(),name='sort'),
    url(r'^tage/(?P<page_id>\d+)$',All_Tage_AritcleView.as_view(),name='tage'),
    url(r'^comment$',AritcleComment.as_view(),name='comment'),
    url(r'^login$',LoginView.as_view(),name='login'),
    url(r'^regisite$', RegisiteView.as_view(), name='Regisite'),
    url(r'^loginout$',LoginOutView.as_view(),name='loginout'),
    url(r'^userinfo$',UserInfoView.as_view(),name='userinfo'),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'templates/js'}),


]
