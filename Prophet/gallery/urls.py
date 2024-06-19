from django.urls import path

from . import views

app_name = "gallery"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.gallery, name="gallery"),

]