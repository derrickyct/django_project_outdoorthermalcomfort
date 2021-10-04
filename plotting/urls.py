from django.conf.urls import url
from . import views
from . import plotting


urlpatterns = [
    url(r'^$', views.PlotGraph, name="plot"),
    url(r'shiny/', views.shiny, name='shiny'),
    url(r'shiny_contents/', views.shiny_contents, name='shiny_contents'),
]

