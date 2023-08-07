from django.urls import path
from .views import *

urlpatterns = [
    path('/', index),
    path('apartment_1', apartment_1),



]