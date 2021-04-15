from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            redirect('registration/login.html')  
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html',context)
    #return render(request, 'register.html',context)

def login_view(request):
    return render(request, 'registration/login.html')
    #return render(request, 'login.html')


