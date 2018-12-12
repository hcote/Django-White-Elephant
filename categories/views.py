from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories, Group
from django.shortcuts import redirect
from .forms import NewGroup, EditProfileForm, EditGroupForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
import datetime

today = datetime.date.today()

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
            group.members.add(User.objects.get(id=group.owner.id))
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

def category_details(request, id):
    category = Categories.objects.get(id=id)
    context = {
        'category': category,
    }
    return render(request, 'categories/category_details.html', context)

def groups(request):
    if request.method == 'POST':
        group_id = request.POST.get('group_id', '')
        print(request.POST)
        group = Group.objects.get(id=group_id)
        user = request.user
        group.save()
        group.members.add(User.objects.get(id=user.id))
        return redirect('/groups')
    else:
        groups = Group.objects.all()
        context = {
            'groups': groups,
            'user': request.user,
            'today': today,
        }
        return render(request, 'categories/groups.html', context)

def edit_group(request, id):
    group = Group.objects.get(id=id)
    if request.method == "POST":
        form = EditGroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            return redirect('/groups/details/' + str(id))
    else:
        form = EditGroupForm(instance=group)
        context = {
            'form': form,
            'group': group,
        }
        return render(request, 'categories/edit_group.html', context)

def group_details(request, id):
    if request.method == 'POST':
        group_id = request.POST.get('group_id', '')
        print(request.POST)
        group = Group.objects.get(id=group_id)
        user = request.user
        group.save()
        group.members.add(User.objects.get(id=user.id))
        return redirect('/groups')
    else:    
        group = Group.objects.get(id=id)
        context = {
            'group': group,
            'today': today,
        }
        return render(request, 'categories/group_details.html', context)

def default_redirect_login_page(request):
    return redirect('/accounts/login')

def profile(request):
    context = {'user': request.user}
    return render(request, 'registration/profile.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'registration/edit_profile.html', context)

def group_delete(request, id):
    if request.method == 'POST':
        Group.objects.get(id = id).delete()
    return redirect('/groups')

def leave_group(request, id):
    if request.method == 'POST':
        user_id = request.POST.get('user_id', '')
        group_id = request.POST.get('group_id', '')
        group = Group.objects.get(id=group_id)
        group.members.remove(user_id)
        group.save()
        return redirect('/groups')


# 'already a member' (instead of join on the group.html)