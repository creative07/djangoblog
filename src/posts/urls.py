from django.contrib import admin
from django.urls import path
from  posts.views import (post_create, post_delete, post_detail, post_list, post_update)



urlpatterns = [
    
    path('', post_list),
    path('create/', post_create),
    path('<int:id>/', post_detail, name="detail"),
    path('update/', post_update),
    path('delete/', post_delete),
    
]