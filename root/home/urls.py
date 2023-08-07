from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('about', about),
    path('testimonial', testimonial),
    path('our_team', our_team),
    path('service', service),
    path('apartment_1', apartment_1),


]