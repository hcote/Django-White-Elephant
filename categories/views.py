from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories
from django.shortcuts import redirect
from .forms import NewGroup

# Create your views here.

# un-comment line below to restrict page access to only logged in users
# @login_required
def index(request):
    if request.method == 'POST':
        form = NewGroup(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'categories/index.html')
        else:
            return HttpResponse('error creating group')
    else:
        categories = Categories.objects.all()
        form = NewGroup()
        context = {
            'categories': categories,
            'form': form,
        }
        return render(request, 'categories/index.html', context)

def details(request, id):
    category = Categories.objects.get(id=id)
    context = {
        'category': category,
    }
    return render(request, 'categories/details.html', context)

def default_redirect_login_page(request):
    return redirect('/accounts/login')