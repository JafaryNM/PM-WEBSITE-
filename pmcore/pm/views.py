from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePage(TemplateView):
    template_name='index.html'


class AboutPage(TemplateView):
    template_name='about.html'


class CoarsePage(TemplateView):
    template_name='coarsecc.html'
    
    
    
class ContactPage(TemplateView):
    template_name='contact.html'
    
class EventPage(TemplateView):
    template_name='events.html'
    
class LoginPage(TemplateView):
    template_name='login.html'