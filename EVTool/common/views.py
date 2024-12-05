from django.views.generic import TemplateView

from EVTool.services.models import Service
from EVTool.vehicles.models import EVCar, EVBike
from EVTool.accounts.models import AppUser


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_authenticated'] = self.request.user.is_authenticated
        context['cars_count'] = EVCar.objects.all().count()
        context['bikes_count'] = EVBike.objects.all().count()
        context['special_offers_count'] = Service.objects.all().count()
        context['users_count'] = AppUser.objects.all().count()
        return context


class UnderConstructionView(TemplateView):
    template_name = 'common/under-construction.html'
