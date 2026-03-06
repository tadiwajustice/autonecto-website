from django.urls import path
from . import views

urlpatterns = [
    path('', views.FleetDashboardView.as_view(), name='fleet_dashboard'),
    path('vehicles/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
]
