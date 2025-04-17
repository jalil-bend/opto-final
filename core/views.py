from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')
