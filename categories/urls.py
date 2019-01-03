from django.urls import path, include
from . import views
from .views import default_redirect_login_page

urlpatterns = [
    path('', default_redirect_login_page),
    path('home', views.index, name='index'),
    path('categories/details/<int:id>/', views.category_details, name='category_details'),
    path('groups/details/<int:id>', views.group_details, name='group_details'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('groups', views.groups, name='groups'),
    path('accounts/profile', views.profile, name='profile'),
    path('accounts/profile/edit', views.edit_profile, name='edit_profile'),
    path('groups/<int:id>/delete', views.group_delete, name = 'group_delete'),
    path('groups/<int:id>/edit', views.edit_group, name='edit_group'),
    path('groups/<int:id>/leave', views.leave_group, name='leave_group'),

]