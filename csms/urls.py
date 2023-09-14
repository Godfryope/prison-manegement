from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    # URLs for Inmates
    path('inmates/', views.inmate_list, name='inmate_list'),
    path('inmates/new/', views.inmate_new, name='inmate_new'),
    path('inmates/<int:inmate_id>/', views.inmate_detail, name='inmate_detail'),
    path('inmates/<int:inmate_id>/edit/', views.inmate_edit, name='inmate_edit'),
    path('inmates/<int:inmate_id>/destroy/', views.inmate_destroy, name='inmate_destroy'),
]