from django.shortcuts import render, redirect
from .models import Apartment
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    transit_data = dict()
    all_apartment = Apartment.objects.all()
    transit_data['all_apartment'] = all_apartment

    return render(request, 'catalog/index.html', {
        'title': 'Квартири',
        'page': 'index',
        'app': 'catalog'
    })


def apartment_1(request):
    return render(request, 'catalog/apartment_1.html', {
        'title': 'Квартира 1',
        'page': 'apartment_1',
        'app': 'catalog'
    })

