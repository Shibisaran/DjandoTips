from django.urls import path
from . import views

app_name = 'tips'

urlpatterns = [
    path('', views.TipListView.as_view(), name='home'),
    path('tip/<int:pk>/', views.TipDetailView.as_view(), name='tip_detail'),
    path('add/', views.TipCreateView.as_view(), name='add_tip'),
] 