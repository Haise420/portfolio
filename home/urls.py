
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('tehnology/', views.tehnology, name="tehnology"),
    path('services/', views.services, name="services"),
    path('course/', views.course, name="course"),


    path('<slug:post_title>', views.pregled_posta, name="pregled_posta"),
    path('project/<slug:projekat_naziv>', views.pregled_projekta, name="pregled_projekta"),

    path('check-website/', views.check_website, name='check-website'),

    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name='logout'),
]