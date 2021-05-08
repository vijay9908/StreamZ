from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('video/<int:video_id>/', views.watch_video, name='watch_video'),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('login/', views.login_view, name="login_url"),
    path('register/', views.register_view, name="register"),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name="logout_url"),
    path('profile/', views.profile, name="profile"),
    # path('<str:session_username>/profile/', views.profile,name="profile"), # for Recommendation Engine @subhash
]
