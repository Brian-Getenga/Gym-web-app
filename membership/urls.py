from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_membership, name='create_membership'),
    path('detail/', views.membership_detail, name='membership_detail'),
    # Add other URL patterns here
]
