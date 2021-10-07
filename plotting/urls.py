from django.conf.urls import url
from . import views
from . import plotting


urlpatterns = [
    url(r'^$', views.plotly, name="plot"),
    url(r'shiny/', views.shiny, name='shiny'),
]
