from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_dashboard, name='member_dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]