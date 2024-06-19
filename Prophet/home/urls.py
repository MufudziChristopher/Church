from django.urls import path

from . import views

app_name = "home"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.home, name="home"),

]