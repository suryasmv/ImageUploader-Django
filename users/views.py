from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def home(request):
    users = User.objects.exclude(username='Surya Challagali').order_by('-id')
    surya = User.objects.get(username='Surya Challagali')
    return render(request, 'home.html', {'user': surya, 'users': users})


def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('views-home')
    else:
        form = UserForm()
    return render(request, 'adduser.html', {'form':form})
