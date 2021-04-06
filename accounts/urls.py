from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('',views.index_view,name='home'),
    path('dashboard/', views.dashboard_view,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.register_view,name="register"),
    path('logout/', LogoutView.as_view(next_page='dashboard'),name="logout_url"),
]