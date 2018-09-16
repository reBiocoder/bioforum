from django.contrib import admin
from django.urls import path,include

from  .views import     Comment_View

app_name='operation'
urlpatterns = [
    path('comment/<int:content_id>',Comment_View.as_view(),name='comment_url'),

   ]