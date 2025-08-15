#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ), 
    
    path(
        'suscripcion/add/', 
        views.Add_suscription,
        name='add-suscription',
    ), 
    
    path(
        'contact/add/', 
        views.Add_contact,
        name='add-contact',
    ), 
]