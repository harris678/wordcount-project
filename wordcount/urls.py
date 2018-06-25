
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.homepage, name = 'home'),
    path('count/',views.count, name = 'count'),
    path('about/',TemplateView.as_view(template_name='about.html'), name='about'),
]
