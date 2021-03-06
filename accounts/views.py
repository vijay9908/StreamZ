from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Video, UserData
from django.core.exceptions import ObjectDoesNotExist   # for further icing @subhash

# Create your views here.

def index_view(request):
    if not request.user.is_authenticated:
        vids = Video.objects.all().order_by('-id')#[:5] # alpha testing - 5 vids available
        context = { "videos" : vids}
        return render(request,'index.html', context)
    else:
        return redirect('dashboard')

def watch_video(request, video_id):
    try:
        video_object = Video.objects.get(id=video_id)
    except ObjectDoesNotExist:
        return render(request, '404.html')
    try:
        session_object = User.objects.get(username = request.user.username)
    except:
        messages.warning(request, "Please Login to watch the video ") # left to Likith & mouni to display message or not
        return redirect('index_view')
    context = {'video': video_object}
    return render(request, 'video.html', context)

@login_required
def dashboard_view(request):
    vids = Video.objects.all().order_by('-id')
    context = { "videos" : vids}
    return render(request, 'dashboard.html', context)
    #return render(request, 'dashboard.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Account registered successfully")
            #return redirect('login_url')
        else:
            pass
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html',context)
    #return render(request, 'register.html',context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def about(request):
    return render(request, 'about.html')
    
def profile(request):  #session_username
    try:
        session_obj = User.objects.get(username = request.user.username)
    except ObjectDoesNotExist:
        return render(request, '404.html')
    profile_data = UserData.objects.get_or_create(user=session_obj)[0]
    context = {'session_obj': session_obj, 'user_data': profile_data}
    return render(request, 'profile.html', context)   #profile stuff - likith handle this space.

def starter_page(request):
    context = {}
    return render(request, 'starter.html', context)

def subscription(request):
    context = {}
    return render(request, 'subscription.html', context)

def payment(request):
    context = {}
    return render(request, 'payment.html', context)

def not_found(request):
    return render(request, '404.html')