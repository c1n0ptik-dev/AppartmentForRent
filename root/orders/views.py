from django.shortcuts import render


def index(request):
    return render(request, 'orders/index.html', {
        'title': 'Барбюса Анри, 28а',
        'page': 'index',
        'app': 'orders'
    })

