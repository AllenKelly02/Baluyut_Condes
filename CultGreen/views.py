from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from .forms import PlantForm

def welcome(request):
    return render(request, 'pages/welcome.html')

def home(request):
    return render(request, 'pages/home.html')


def search(request):
    return render(request, 'pages/search.html')

def myplants(request):
    plants = Plant.objects.all()
    return render(request, 'pages/myplants.html', {'plants': plants})

def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myplants')
    else:
        form = PlantForm()
    return render(request, 'crud-modal', {'form': form})

def edit_plant(request):
    return render(request, 'pages/edit_plant.html')

def edit_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('myplants')
    else:
        form = PlantForm(instance=plant)
    return render(request, 'pages/edit_plant.html', {'form': form, 'plant': plant})

def delete_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    plant.delete()
    return redirect('myplants')


def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')