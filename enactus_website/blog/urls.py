from django.urls import path
from . import views
urlpatterns = [
    path('discussion/', views.BlogListView.as_view(), name='discussion'),
    path('discussion/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('discussion/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('discussion/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('discussion/<int:pk>/delete/',views.BlogDeleteView.as_view(), name='post_delete'),
]