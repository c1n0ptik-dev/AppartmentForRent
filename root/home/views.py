from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {
        'title': 'Головна',
        'page': 'index',
        'app': 'home'
    })


def about(request):
    return render(request, 'home/about.html', {
        'title': 'ПРо сайт',
        'page': 'about',
        'app': 'home'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'title': 'Контакти',
        'page': 'contacts',
        'app': 'home'
    })


def testimonial(request):
    return render(request, 'home/testimonial.html', {
        'title': 'Відгук',
        'page': 'testimonial',
        'app': 'home'
    })


def our_team(request):
    return render(request, 'home/our_team.html', {
        'title': 'Наша команда',
        'page': 'our_team',
        'app': 'home'
    })


def service(request):
    return render(request, 'home/service.html', {
        'title': 'Сервис',
        'page': 'service',
        'app': 'home'
    })


def apartment_1(request):
    return render(request, 'home/apartment_1.html', {
        'title': 'Барбюса Анри, 28а',
        'page': 'apartment_1',
        'app': 'home'
    })

def apartment_2(request):
    return render(request, 'home/apartment_2.html', {
        'title': 'Мишуги Олександра, 1/4',
        'page': 'apartment_2',
        'app': 'home'
    })

def orders2(request):
    return render(request, 'home/orders2.html', {
        'title': 'Мишуги Олександра, 1/4',
        'page': 'orders2',
        'app': 'home'
    })

def apartment_3(request):
    return render(request, 'home/apartment_3.html', {
        'title': 'Юрія Іллєнка, 83',
        'page': 'apartment_3',
        'app': 'home'
    })

def orders3(request):
    return render(request, 'home/orders3.html', {
        'title': 'Юрія Іллєнка, 83',
        'page': 'orders3',
        'app': 'home'
    })