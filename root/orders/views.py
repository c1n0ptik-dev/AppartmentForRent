from django.shortcuts import render


def index(request):
    return render(request, 'orders/index.html', {
        'title': 'Бронювання',
        'page': 'index',
        'app': 'orders'
    })