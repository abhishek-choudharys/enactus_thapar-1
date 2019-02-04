from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.SignUPView.as_view(),name='signup'),
    path('edit/',views.EditUser,name='edit_profile'),
    path('password-change/',views.ChangePassword,name='password-change')
]

