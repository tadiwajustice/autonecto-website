from django.views.generic import TemplateView

class FleetDashboardView(TemplateView):
    template_name = "fleet/fleet_dashboard.html"

class VehicleListView(TemplateView):
    template_name = "fleet/vehicle_list.html"

class VehicleDetailView(TemplateView):
    template_name = "fleet/vehicle_detail.html"
