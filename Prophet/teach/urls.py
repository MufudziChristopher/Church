from django.urls import path

from . import views

app_name = "teach"


urlpatterns = [
    #Leave as empty string for base url

    #------------ (STORE - URLS) ------------

	path('', views.teach, name="teach"),
	path('scroll', views.scroll, name="scroll"),

]