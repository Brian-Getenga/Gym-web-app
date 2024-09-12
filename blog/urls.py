""" from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:id>/', views.blog_post_detail, name='blog_post_detail'),
]
 """

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('category/<int:category_id>/', views.blog_list, name='blog_list_by_category'),
    path('blog/<int:id>/', views.blog_post_detail, name='blog_post_detail'),
    path('<int:post_id>/bookmark/', views.bookmark_post, name='bookmark_post'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
]
