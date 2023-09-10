from django.shortcuts import render
from django.views import generic
from . import models


class HomeView(generic.TemplateView):
    """
    Display the Home Page
    """
    template_name = 'main/index.html'


class AboutView(generic.TemplateView):
    """
    Display the About Page
    """
    template_name = 'main/about.html'


class LocationView(generic.ListView):
    """
    Display contact information for each restaurant location registered in the
    database.
    """
    template_name = 'main/contact.html'
    queryset = models.Location.objects.order_by('city')


class MenuView(generic.ListView):
    """
    Display the Menu Page with the Menu Items from the database sorted by type
    """
    queryset = models.MenuItem.objects.order_by('-date_added')
    template_name = 'main/menu.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types'] = models.MENU_CATEGORIES

        return context


class MenuItemDetailView(generic.DetailView):
    """
    Display the details of the specified menu item
    """
    model = models.MenuItem
    template_name = 'main/menu_item_detail.html'


class ReserveView(generic.TemplateView):
    template_name = 'main/reserve.html'
