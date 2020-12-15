from django.conf.urls import url
from . import views
from .views import TestView

#app_name = 'MySite'

urlpatterns = [
    url(r'home/', views.index, name='index'),
    url(r'^about/(?P<id>\d+)/$', views.about, name='about'),
    url(r'^delete/(?P<id>\d+)/$', views.delete_data, name='delete'),
    url(r'contact/', views.contact, name='contact'),   
    url(r'test/', TestView.as_view(), name='testData')
     
]
