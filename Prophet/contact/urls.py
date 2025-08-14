from django.urls import path

from . import views

app_name = "contact"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.contact, name="contact"),

]