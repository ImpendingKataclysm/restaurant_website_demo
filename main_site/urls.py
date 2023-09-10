from django.urls import path
from . import views

app_name = 'main_site'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.LocationView.as_view(), name='contact'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('reserve/', views.ReserveView.as_view(), name='reserve'),
    path('detail/<int:pk>', views.MenuItemDetailView.as_view(), name='menu_item')
]
