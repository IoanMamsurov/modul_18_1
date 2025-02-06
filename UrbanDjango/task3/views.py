from django.shortcuts import render


def index(request):
    text = 'Главная страница'
    head = 'Главная'
    first = 'Магазин'
    second = 'Корзина'
    context = {
        'text': text,
        'head': head,
        'first': first,
        'second': second,
    }
    return render(request, 'third_task/head.html', context)


def first(request):
    title = 'Магазин'
    one = 'Первый товар'
    two = 'Второй товар'
    there = 'Третий товар'
    button = 'Купить'
    button_2 = 'Вернуться на главную'
    context = {'title': title, 'one': one, 'two': two, 'there': there, 'button': button, 'button_2': button_2}
    return render(request, 'third_task/first.html', context)

def second(request):
    title = 'Корзина'
    button_3 = 'Вернуться на главную'
    button_4 = 'Вернуться в магазин'
    text = 'Корзина пуста'
    context = {
        'text': text,
        'button_3': button_3,
        'button_4': button_4,
        'title': title,
    }
    return render(request, 'third_task/second.html', context)
