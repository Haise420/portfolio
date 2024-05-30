
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('tehnology/', views.tehnology, name="tehnology"),
    path('services/', views.services, name="services"),
    path('course/', views.course, name="course"),


    path('<slug:post_title>', views.pregled_posta, name="pregled_posta"),
]