from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id :{cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug :{cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect('/')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')