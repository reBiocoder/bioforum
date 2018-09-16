# -*- coding: utf-8 -*-

__author__ = 'Echor'

__date__ = 2018 / 9 / 11


from django.contrib import admin
from django.urls import path,include

from  .views import   Theme1_View,PubTopic_View,Index_View,default_index,Topic_Content_View


app_name='topic'
urlpatterns = [
    path('',default_index,name='index'),
    path('create/<str:username>/',PubTopic_View.as_view(),name='create_topic'),
    path('page/<int:page_id>/',Index_View.as_view(),name='page'),
    path('content/<int:content_id>/',Topic_Content_View.as_view(),name='topic_content'),
    path('theme/<int:theme_id>/',Theme1_View.as_view(),name='theme1'),
]