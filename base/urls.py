from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('papers/', views.papers, name='papers'),
    path('speakers/', views.speakers, name='speakers'),
    path('reservations/', views.reservations, name='reservations'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('user/<str:pk>', views.userProfilePage, name='profile'),
    # path('update/<str:pk>', views.updateUser, name='updateUser')
]