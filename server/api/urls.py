from django.urls import path
from server.api import views
from server.modules.apps import get_urls

# /api
urlpatterns = [
    path('register', views.register),
    path('addr', views.addr),
    path('discovery', views.modules_discovery),
] + get_urls("api")