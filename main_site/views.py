from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    """
    Display the Home Page
    """
    template_name = 'main/index.html'


class AboutView(generic.TemplateView):
    template_name = 'main/about.html'


class ContactView(generic.TemplateView):
    template_name = 'main/contact.html'


class MenuView(generic.TemplateView):
    template_name = 'main/menu.html'


class ReserveView(generic.TemplateView):
    template_name = 'main/reserve.html'
