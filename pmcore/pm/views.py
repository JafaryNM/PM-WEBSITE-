from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView,ListView


# Create your views here.
class ArticlesList(ListView):
    
    template_name='index.html'
    model=Blog
    def get_context_data(self, **kwargs):
        context = super(ArticlesList, self).get_context_data(**kwargs)
        context['blogs']=Blog.objects.all()
        return context


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