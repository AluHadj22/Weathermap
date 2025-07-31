import requests 
from django.shortcuts import render 
from .forms import CityForm 
 
def index(request): 
    appid = '594cf78aebd17591b564bee1d57fe801' # передаю свой ключ из openweather 
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=' + appid # добавляю свой ключ к юрл(он тоже взят из openweather конечно же) 
 
    if request.method == 'POST': # проверяю, является ли метод отправки данных Post, а не get 
        form = CityForm(request.POST) 
         
        if form.is_valid():# опять же, если форма и правда передает пост запрос, то выполняется код 
            city_name = form.cleaned_data['city_name'] 
            resp = requests.get(url.format(city_name)).json()  
            #создаю словарь, который берет данные  по юрл через гет запрос, благодаря библиотеке requests. Полученные данные можно сделать словарем 
            #У этого словаря есть индексы, они в самом джейсоне привязаны как ключ - значение. Поэтому,  main - это ключ, а его значение pressure(а у него свое значение) 
            # все эти данные находятся в json файле, который можно получить на openweathermap. - Только я не смог найти вероятность дождя, ни в json, ни на самом сайте. 
            city_all_info = { 
                'city': city_name, 
                'temp': int(resp["main"]["feels_like"]), 
                'wind': int(resp["wind"]["speed"]), 
                'pres': int(resp["main"]["pressure"]), 
                'humidity': resp["main"]["humidity"], 
            } 
 
            context = {'info': city_all_info}# сохраняю в переменную данные словаря, чтобы передать в index.html как словарь - info(ключ) - city_all_info - значение 
            return render(request, 'weather/index.html', context) # возвращаю это все и указываю в какой папке лежит index.html 
    else: 
        form = CityForm() 
 
    context = {'form': form} 
    return render(request, 'weather/index.html', context)
