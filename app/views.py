from django.shortcuts import render, redirect
from django.db.models import Q

from .models import News, Category, Color, Car
from .forms import CarCreateForm


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
    categories = Category.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        model = request.POST['model']
        year = request.POST['year']
        description = request.POST['description']
        odometer = request.POST['odometer']
        engine_capacity = request.POST['engine_capacity']
        color_id = request.POST['color_id']
        category_id = request.POST['category_id']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car = Car(title=title, category=category, model=model, year=year, odometer=odometer,
                  engine_capacity=engine_capacity, color=color, image=image, description=description)
        car.save()

        return redirect('news_create')

    return render(request, 'app/car_create.html', {"categories": categories, "colors": colors})


def car_create_views_2(request):

    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = CarCreateForm()

    return render(request, 'app/car_create_2.html', {'form': form})