from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('internships/', views.internships, name='internships'),
    path('analytics/', views.analytics, name='analytics'),
    path('settings/', views.settings_page, name='settings'),
    path('contact/', views.contact, name='contact'),
]