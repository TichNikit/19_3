from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegister
from .models import *


# Create your views here.



def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    buyers_list = [buyer.name for buyer in buyers]
    context = {
        'Buyer': buyers
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if password == repeat_password and age >= 18 and username not in buyers_list:
            Buyer.objects.create(name=username, age=age)
            return HttpResponse(f'Приветствуем, {username}')
        elif username in buyers_list:
            return HttpResponse('Пользователь уже существует')
        elif password != repeat_password:
            return HttpResponse('Пароли не совпадают')
        elif age < 18:
            return HttpResponse('Вы должны быть старше 18')
        else:
            return HttpResponse('Что-то невообразимое')
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    buyers = Buyer.objects.all()
    buyers_list = [buyer.name for buyer in buyers]
    context = {
        'Buyer': buyers
    }
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info['username'] = username
            info['age'] = age

            if password == repeat_password and age >= 18 and username not in buyers_list:
                Buyer.objects.create(name=username, age=age)
                return HttpResponse(f'Приветствуем, {username}')
            elif username in buyers_list:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
    # else:
    #     form = UserRegister()
    #     info['form'] = form


    return render(request, 'registration_page.html', context=info)



def films(request):
    return render(request, 'main.html')

def cinemas(request):
    game = Game.objects.all()
    context ={
        'games': game
    }
    return render(request, 'game.html', context)

def tickets(request):
    return render(request, 'ticket.html')