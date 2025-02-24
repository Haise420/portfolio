
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('tehnology/', views.tehnology, name="tehnology"),
    path('services/', views.services, name="services"),
    path('course/', views.course, name="course"),
    path('account/', views.account, name="account"),



    path('<slug:post_title>', views.pregled_posta, name="pregled_posta"),
    path('project/<slug:projekat_naziv>', views.pregled_projekta, name="pregled_projekta"),

    path('check-website/', views.check_website, name='check-website'),

    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name='logout'),

    


    path('administracija/', views.administracija, name="administracija"),
    path('administracija/pregled-projekata/', views.pregled_projekata, name="pregled_projekata"),
    path('administracija/pregled-projekta/<int:projekat_id>', views.admin_pregled_projekta, name="pregled_projekta"),
    path('administracija/pregled-tehnologija/', views.pregled_tehnologija, name="pregled_tehnologija"),
    path('administracija/pregled-kurseva/', views.pregled_kurseva, name="pregled_kurseva"),
    path('administracija/pregled-postova/', views.pregled_postova, name="pregled_postova"),
    path('administracija/pregled-posta/<int:post_id>/', views.pregled_posta, name="pregled_posta"),
    path('administracija/pregled-korisnika/', views.pregled_svih_korisnika, name="pregled_korisnika"),
    path('administracija/pregled-korisnika/<int:korisnik_id>/', views.pregled_korisnika, name="pregled_korisnik"),
    


]


