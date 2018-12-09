from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories, Group
from django.shortcuts import redirect
from .forms import NewGroup
from django.contrib.auth.models import User

# Create your views here.

# un-comment line below to restrict page access to only logged in users
# @login_required
def index(request):
    if request.method == 'POST':

        form = NewGroup(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
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

def groups(request):
    if request.method == 'POST':
        print('hello')
        group_id = request.POST.get('group_id', '')
        print(request.POST)
        group = Group.objects.get(id=group_id)
        user = request.user
        group.save()
        group.members.add(User.objects.get(id=user.id))
        return render(request, 'categories/index.html')
    else:
        groups = Group.objects.all()
        context = {
            'groups': groups
        }
        return render(request, 'categories/groups.html', context)

def default_redirect_login_page(request):
    return redirect('/accounts/login')