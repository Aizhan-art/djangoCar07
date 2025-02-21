from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('news_create/', views.news_create_view, name='news_create'),
    path('car_create/', views.car_create_view, name='car_create'),
    path('car_detail/<int:pk>/', views.car_detail_view, name='detail'),
    path('car_delete/<int:pk>/', views.car_delete, name='delete'),
]