from django.urls import path
from app import views

urlpatterns = [
    path('sync/', views.easy),
    path('async/', views.aeasy),
    path('sync/hard/', views.hard),
    path('async/hard/', views.ahard),
    path('sync/api/', views.sync_with_api),
    path('async/api/', views.async_with_api),
    path('sync/sleep/', views.sync_sleep),
    path('async/sleep/', views.async_sleep),
]