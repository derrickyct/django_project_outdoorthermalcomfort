from django.conf.urls import url
from . import views
from . import plotting


urlpatterns = [
    url(r'^$', views.PlotGraph, name="plot"),
]

