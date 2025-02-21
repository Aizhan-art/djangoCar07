from django.shortcuts import render, redirect
from django.db.models import Q

from .models import News, Category, Color,Car
from .forms import CarForm


def index_view(request):
    cars = Car.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        cars = Car.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
    return render(request, 'app/index.html', {'cars': cars})


def news_create_view(request):

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        news = News(title=title, description=description)
        news.save()

    return render(request, 'app/news_create.html')

def car_create_view(request):

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = CarForm()

    return render(request, 'app/car_create.html', {'form': form})


def car_detail_view(request, pk):
    car = Car.objects.get(id=pk)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("detail", car.id)

    form = CarForm(instance=car)

    return render(request, 'app/car_detail.html', {'car': car, 'form': form})

def car_delete(request, pk):
    car = Car.objects.get(id=pk)
    car.delete()

    return redirect('index')
