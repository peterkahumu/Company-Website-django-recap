from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['inventory_list'] = ['FlatBread', 'Sweet Potatoes', 'Deep fried dough (Mandazi)', 'Eggs']
        context['title'] = 'Home'
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['address'] = "123 Johnson Street"
        context['phoneNumber'] = '+25412345678'
        context['title'] = "About"
        return context