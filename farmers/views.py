# farmers/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

import farmers
from .forms import FarmerRegistrationForm, FarmerLoginForm,ChooseStateForm
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            state = form.cleaned_data['state']
            location = form.cleaned_data['location']
            login(request, user)
            return redirect('choose_state', username=user.username)
    else:
        form = FarmerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def choose_state(request, username):
    # Implement logic to choose state using location algorithm
    # For simplicity, we'll use a predefined list of states
    states = ['State1', 'State2', 'State3']
    return render(request, 'choose_state.html', {'states': states, 'username': username})


def login_user(request):
    if request.method == 'POST':
        form = FarmerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('choose_state', username=username)
    else:
        form = FarmerLoginForm()
    return render(request, 'login.html', {'form': form})

def nearby_markets(request, username, state):
    # Implement logic to find nearby markets
    # For simplicity, we'll use a predefined list of markets
    markets = ['Market1', 'Market2', 'Market3']
    return render(request, 'nearby_markets.html', {'markets': markets, 'username': username, 'state': state})

def choose_crop_type(request, username, state, market):
    # Implement logic to choose crop type
    # For simplicity, we'll use a predefined list of crop types
    crop_types = ['Crop1', 'Crop2', 'Crop3']
    return render(request, 'choose_crop_type.html', {'crop_types': crop_types, 'username': username, 'state': state, 'market': market})

def display_prices(request, username, state, market, crop_type):
    # Implement logic to display prices
    # For simplicity, we'll use dummy prices
    price_today = 10.5
    price_last_10_days = [9.5, 10.0, 11.0, 10.2, 9.8, 10.5, 10.3, 10.8, 11.2, 10.6]
    
    # Save data to the database
    farmer = farmers.objects.create(username=username, state=state, location=market, crop_type=crop_type, price_today=price_today, price_last_10_days=price_last_10_days)
    farmer.save()

    return render(request, 'display_prices.html', {'username': username, 'state': state, 'market': market, 'crop_type': crop_type, 'price_today': price_today, 'price_last_10_days': price_last_10_days})

def home(request):
    return render(request, 'home.html')