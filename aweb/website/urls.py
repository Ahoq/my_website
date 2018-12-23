from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'website-home'),
    path('about/', views.about, name = 'website-about'),
    path('email/', views.email, name = 'website-email'),
    path('thanks/', views.mail, name = 'thanks'),

]
