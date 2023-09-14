from django.urls import path, re_path
from django.contrib import admin
from csms.views import *
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inmate_list, name='home'),  # Update to inmate_list view
    path('inmates/new/', inmate_new, name='inmate_new'),  # New URL for creating a new inmate
    re_path(r'^inmates/(?P<inmate_id>\d+)/$', inmate_detail, name='inmate_detail'),  # New URL for inmate detail
    re_path(r'^inmates/edit/(?P<inmate_id>\d+)/$', inmate_edit, name='inmate_edit'),  # New URL for editing inmate
    re_path(r'^inmates/delete/(?P<inmate_id>\d+)/$', inmate_destroy, name='inmate_destroy'),  # New URL for deleting inmate
    # path('officers/', officer_list, name='officer_list'),  # New URL for officer list
    # path('officers/new/', officer_new, name='officer_new'),  # New URL for creating a new officer
    # re_path(r'^officers/(?P<officer_id>\d+)/$', officer_detail, name='officer_detail'),  # New URL for officer detail
    # re_path(r'^officers/edit/(?P<officer_id>\d+)/$', officer_edit, name='officer_edit'),  # New URL for editing officer
    # re_path(r'^officers/delete/(?P<officer_id>\d+)/$', officer_destroy, name='officer_destroy'),  # New URL for deleting officer
    path('users/login/', auth.LoginView.as_view(template_name='login.html'), name='login'),
    path('users/logout/', auth.LogoutView.as_view(next_page='/'), name='logout'),
    path('users/change_password/', login_required(auth.PasswordChangeView.as_view(success_url='/')), name='change_password'),
]
