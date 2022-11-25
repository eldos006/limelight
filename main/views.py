from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import DetailView, UpdateView, DeleteView
from main.forms import LimelightForm, NewsForm
from main.models import Car, News


#Главная НАЧАЛО
def home(request):
    data = Car.objects.order_by("id")[:3]
    return render(request, 'main/home.html', {'data': data})


def home_home(request):
    data = Car.objects.all()
    return render(request, 'main/home,html', {'data':data})
#Главная КОНЕЦ


#News НАЧАЛО
def news(request):
    data = News.objects.all()
    return render(request, 'main/news.html', {'data': data})


def more_news(request):
    data = News.objects.all()
    return render(request, 'main/more-news.html', {'data': data})


def news_form(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            print('keldi')
            form.save()
            return redirect('home')
        else:
            error = 'Запись было неверной'

    form = NewsForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/news_form.html', data)
#News КОНЕЦ


#Car НАЧАЛО
def index(request):
    data = Car.objects.all()
    return render(request, 'main/index.html', {'data': data})


def more(request, id):
    data = Car.objects.get(id=id)
    return render(request, 'main/more.html', {'data': data})


def profile(request, id):
    data = Car.objects.get(id=id)
    return render(request, 'main/more.html', {'data': data})


def form(request):
    error = ''
    if request.method == 'POST':
        form = LimelightForm(request.POST, request.FILES)
        if form.is_valid():
            print('keldi')
            form.save()
            return redirect('home')
        else:
            error = 'Запись было неверной'


    form = LimelightForm()
    data = {
        'form':form,
        'error':error,
    }
    return render(request, 'main/form.html', data)
#Car КОНЕЦ


#Редактирование, Удаление, Detail
class NewsDetailView(DetailView):
    model = Car
    template_name = 'main/more.html'
    context_object_name = 'car'


def del_view(request, pk):
    Car.objects.get(id=pk).delete()

    return redirect("/index/")


