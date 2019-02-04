from django.urls import path
from .views import homepage,ProfileView

urlpatterns = [
    path('',homepage.as_view(), name='index'),
    path('profile/',ProfileView.as_view(),name='profile')
]
