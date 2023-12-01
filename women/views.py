from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    if request.GET:
        print(request)
    return HttpResponse('Страница приложения Women')

def header(request, catid):
    return HttpResponse(f'<h1>Заголовок для категории {catid}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>по адрессу {request.build_absolute_uri()} нет такой страницы</h1>')