from django.urls import path

from . import views

app_name = "story"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.story, name="story"),

]