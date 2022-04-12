from django.urls import path
from django.conf import settings
from .views import *
urlpatterns = [
    path('',ArticlesList.as_view(), name='index'),
    path('about/',AboutPage.as_view(), name='about'),
    path('coarsecc/',CoarsePage.as_view(), name='coarsecc'),
    path('contact/',ContactPage.as_view(), name='contact'),
    path('events/', EventPage.as_view(), name='events'),
    path('login/',LoginPage.as_view(), name='login')
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)