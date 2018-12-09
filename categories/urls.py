from django.urls import path, include
from . import views
from .views import default_redirect_login_page

urlpatterns = [
    path('', default_redirect_login_page),
    path('home', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('groups', views.groups, name='groups'),
    path('accounts/profile', views.profile, name='profile'),
    path('accounts/profile/edit', views.edit_profile, name='edit_profile')    
]