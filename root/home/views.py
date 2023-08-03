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