import random
from faker import Faker
from django.shortcuts import render

def lotto2(request):
    numbers = random.sample(range(1,46), 6)
    context = {
        'numbers' : numbers
    }
    return render(request, 'lotto2.html', context)
# Create your views here.

def profile2(request, username):
    context = {
        'name' : username
    }
    return render(request,'profile2.html', context)

def phone_books(request):
    fake = Faker()
    phone_books = {}
    for i in range(50):
        phone_books[fake.phone_number()] = fake.name()
    context = {
        'phone_books': phone_books,
    }
    return render(request, 'phone_books.html', context)

def god(request, myname):
    my_list = ['귀여움', '멍청함', '카리스마', '식욕', '웃김', '못생김', '찐따', '뚱땡이', '멋짐', '잘생김', '날씬', '몸짱', '잇팁']
    style = random.sample(my_list, 3)
    context = {
        'style1': style[0],
        'style2': style[1],
        'style3': style[2],
        'myname': myname
    }
    return render(request, 'god.html', context)