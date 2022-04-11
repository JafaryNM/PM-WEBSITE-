from django.urls import path
from .views import *
urlpatterns = [
    path('',HomePage.as_view(), name='home'),
    path('about/',AboutPage.as_view(), name='about'),
    path('coarsecc/',CoarsePage.as_view(), name='coarsecc'),
    path('contact/',ContactPage.as_view(), name='contact'),
    path('events/', EventPage.as_view(), name='events'),
    path('login/',LoginPage.as_view(), name='login')
]