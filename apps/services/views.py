from django.views.generic import ListView, DetailView
from .models import Service

class ServiceListView(ListView):
    model = Service
    template_name = "services/services_list.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "services/service_detail.html"
    context_object_name = "service"

    # Convert features (text) into a list  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        features_text = self.object.features or ""
        context["features"] = features_text.split("\n")
        return context
