from django.shortcuts import render

def index(request):
    return render(request, 'app_test/index.html')

def contacts(request):
    return render(request, 'app_test/contacts.html')

def add(request):
    return render(request, 'app_test/add.html')

def prices(request):
    return render(request, 'app_test/prices.html')

def spares(request):
    return render(request, 'app_test/spares.html')
