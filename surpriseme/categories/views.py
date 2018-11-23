from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories

# Create your views here.

# un-comment line below to restrict page access to only logged in users
# @login_required
def index(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories/index.html', context)

def details(request, id):
    category = Categories.objects.get(id=id)
    context = {
        'category': category
    }

    return render(request, 'categories/details.html', context)
