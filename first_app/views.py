import random
from faker import Faker
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html') #html을 rendering을 해주는 역할
                    
def hello(request):
    my_name = 'junny'
    context ={
        'my_name': my_name#'junny',
    }

    return render(request, 'hello.html', context)
    # return render(request, 'hello.html', {'my_name': 'junny'})

def lunch(request):
    menu = ['짜장면', '불닭볶음면', '마라탕']
    pick = random.choice(menu)
    context = {
        'pick' : pick #'딕셔너리이름' : 변수
    }
    return render(request, 'lunch.html', context)

def lotto(request):
    lotto_num = random.sample(range(1, 46), 6)
    context ={
        'lotto_num' : lotto_num 
    }
    return render(request, 'lotto.html', context)

def profile(request, username):
    context = {
        'username' : username,
    }
    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3
    context = {
        'number' : number,
        'result' : result
    }
    return render(request, 'cube.html', context)

def articles(request):
    fake = Faker()
    fake_articles = []

    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }
    return render(request, 'articles.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # print(request.GET['title']) #안녕
    # print(request.GET['content']) #방가
    title = request.GET.get('title')
    content = request.GET.get('content') 
    #get: keyerror가 발생하지 않음
    #key가 dict에 없으면 'None'을 출력

    context = {
        'title': title,
        'content': content,
    }
    return render(request, 'pong.html', context)