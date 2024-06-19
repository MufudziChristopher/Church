from django.urls import path

from . import views

app_name = "videos"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.videos, name="videos"),

]