from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import Bayer, Game, News
from django.core.paginator import Paginator

# Create your views here.
def func_template(request):
    title = 'Главная страница'
    text_1 = 'Главная'
    text_2 = 'Магазин'
    text_3 = 'Корзина'
    context = {
        'title': title,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3,
        'news': news_function,
    }
    return render(request,'main_page.html', context)

def func_template_first(request):   #отображение записей из таблицы Game
    games = Game.objects.all()  # заполнение списка games записями из таблицы Game
    context = {
        'games': games,
    }
    return render(request,'first_page.html',context)

def func_template_second(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'second_page.html', context)

users = [] #Пользователи
info = {}  #функция render
bayers = list(Bayer.objects.all()) #заполнение списка bayers записями из таблицы Bayer
for i in range(Bayer.objects.count()):
    users.append(bayers[i].name) #заполннеие списка users именами пользователецй изтабл. Bayer

#Create your views here.
def sign_up_by_django(request):
    if request.method =='POST':
        form = UserRegister(request.POST)
        if form.is_valid():     #проверка корректности
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            contex = {
                'info': info,
                'form': form,
            }
            if password == repeat_password and int(age) >= 18 and username not in users:
                Bayer.objects.create(name=username, age=age)
                return HttpResponse(f"Приветствуем, {username}!")
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', contex)
            # if int(age) < 18:
            #     info['error'] = 'Вы должны быть старше 18'
            #     return render(request, 'registration_page.html', contex)
            if username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', contex)
    else:
        form = UserRegister()
    return render(request,'registration_page.html',{'form': form})

def sign_up_by_html(request):                  #главная стpаница
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        subscribe = request.POST.get('subscribe') == 'on'
        contex = {
            'info': info,
        }
        if password == repeat_password and username not in users:
            Bayer.objects.create(name=username, balance=100, age=age)
            return HttpResponse(f"Приветствуем, {username}!")
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request,'registration_page.html',contex)
        # if int(age) < 18:
        #     info['error'] = 'Вы должны быть старше 18'
        #     return render(request,'registration_page.html',contex)
        if username in users:
            info['error'] = 'Пользователь уже существует'
            return render(request,'registration_page.html',contex)

    return render(request,'registration_page.html')

def news_function(request):
    post = News.objects.all()                   #получаем все новости
    paginator = Paginator(post, 3)      #создаем пагинатор
    page_number = request.GET.get('page')       #получаем номер страницы, на котрую переходит пользователь
    news = paginator.get_page(page_number)      #получаем новости для текущей страницы
    context = {
        'news': news,
    }
    return render(request, 'news.html', context) #передаем контекст в шаблон