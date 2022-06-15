from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('addven/', views.AddVenue, name='add_venueurl'),
    path('showven/', views.ShowVenue, name='show_venueurl'),
    path('del/<int:id>', views.DelView, name='delete_venue')
    ]