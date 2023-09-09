from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    """
    Display the Home Page
    """
    template_name = 'main/index.html'
