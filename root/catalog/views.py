from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html', {
        'title': 'Каталог',
        'page': 'index',
        'app': 'catalog'
    })


def apartment_1(request):
    return render(request, 'catalog/apartment_1.html', {
        'title': 'Квартира 1',
        'page': 'apartment_1',
        'app': 'catalog'
    })

