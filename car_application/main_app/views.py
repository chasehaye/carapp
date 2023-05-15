from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ServiceForm
from .models import Car, Upgrade
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    service_form = ServiceForm()
    id_list = car.upgrade.all().values_list('pk')
    upgrades_car_doesnt_have = Upgrade.objects.exclude(id__in=id_list)
    return render(request, 'main_app/car_detail.html', {
        'car': car,
        'service_form': service_form,
        'upgrades_car_doesnt_have': upgrades_car_doesnt_have
    })
class CarList(ListView):
    model = Car
class CarCreate(CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'description']
class CarUpdate(UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'color', 'description']
class CarDelete(DeleteView):
    model = Car
    success_url = '/cars'

def add_service(request, car_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit = False)
        new_service.car_id = car_id
        new_service.save()
    return redirect('car_detail', pk=car_id)

class UpgradeList(ListView):
    model = Upgrade
class UpgradeDetail(DetailView):
    model = Upgrade
class UpgradeCreate(CreateView):
    model = Upgrade
    fields = ['name', 'description', 'cost']
class UpgradeUpdate(UpdateView):
    model = Upgrade
    fields = ['name', 'description', 'cost']
class UpgradeDelete(DeleteView):
    model = Upgrade
    success_url = '/upgrades'

def assoc_upgrade(request, car_id, upgrade_id):
    Car.objects.get(id=car_id).upgrade.add(upgrade_id)
    return redirect('car_detail', pk=car_id)
def unassoc_upgrade(request, car_id, upgrade_id):
    Car.objects.get(id=car_id).upgrade.remove(upgrade_id)
    return redirect('car_detail', pk=car_id)

def signup(request):
    error_message = '' 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car_list')
        else:
            error_message = 'Invalid Sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)