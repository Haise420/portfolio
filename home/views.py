from django.shortcuts import render, redirect, get_object_or_404
from .models import *
import requests
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout


# Create your views here.
def home(request):

    projekti = Projekat.objects.all()
    postovi = Post.objects.all()

    context = {
        'projekti': projekti,
        'postovi': postovi,
        
    }

    return render(request, 'home/home.html', context)


def projects(request):

    projekti = Projekat.objects.all()

    context = {'projekti': projekti,}

    return render(request, 'home/projects.html', context)

def tehnology(request):



    context = {}

    return render(request, 'home/tehnology.html', context)

def services(request):

    context = {}

    return render(request, 'home/services.html', context)

def course(request):

    kursevi = Kurs.objects.all()

    context = {'kursevi': kursevi}

    return render(request, 'home/course.html', context)

def pregled_posta(request, post_title):

    post = get_object_or_404(Post, slug=post_title)

    context = {'post': post}

    return  render(request, 'home/view_post.html', context)



def pregled_projekta(request, projekat_naziv):

    print(projekat_naziv)

    projekat = get_object_or_404(Projekat, slug=projekat_naziv)

    context = {'projekat': projekat}

    return  render(request, 'home/view_project.html', context)


def register(request):

    if request.method == "POST":
        
        ime = request.POST.get("username")
        sifra = request.POST.get("password")

        novi_korisnik = User(username=ime, password=sifra)
        novi_korisnik.save()
        
        return redirect('login')
    
    return render(request, 'home/register.html')

def login(request):

    context = {} 

    if request.method == 'POST':

        ime = request.POST.get('username')
        sifra = request.POST.get('password')


        user = authenticate(request, username=ime, password=sifra)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Preusmeri na željenu stranicu nakon prijave
        else:
            context['error'] = 'Pogrešno korisničko ime ili lozinka.'

    if not context:
        context = None
 
    return render(request, 'home/login.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')


def check_website(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        url = data.get('url')
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return JsonResponse({'status': 'online'})
            else:
                return JsonResponse({'status': 'offline'})
        except requests.RequestException:
            return JsonResponse({'status': 'offline'})
    return JsonResponse({'status': 'error'})

def account(request):


    return render(request, 'home/account.html')

def administracija(request):


    return render(request, 'administracija/home.html')

def pregled_projekata(request):

    projekti = Projekat.objects.all()
    context = {'projekti': projekti}

    return render(request, 'administracija/projekti.html', context)



def admin_pregled_projekta(request, projekat_id):

    projekat = Projekat.objects.get(id=projekat_id)

    context = {'projekat': projekat}

    return  render(request, 'administracija/projekat.html', context)



def pregled_tehnologija(request):

    tehnologije = Tehnologija.objects.all()
    context = {'tehnologije': tehnologije}

    return render(request, 'administracija/tehnologije.html', context)

def pregled_kurseva(request):
   
    kursevi = Kurs.objects.all()
    context = {'kursevi': kursevi}

    return render(request, 'administracija/kursevi.html', context)

def pregled_postova(request):


    # x je informacija koju saljes u contextu
    postovi = Post.objects.all()

    context = {'postovi': postovi}

    return render(request, 'administracija/postovi.html', context)


def pregled_posta(request, post_id):


    # x je informacija koju saljes u contextu
    post = Post.objects.get(id=post_id)

    context = {'post': post}

    return render(request, 'administracija/post.html', context)

def pregled_svih_korisnika(request):

    korisnici = Korisnik.objects.all()
    context = {'korisnici': korisnici}

    return render(request, 'administracija/korisnici.html', context)

def pregled_korisnika(request, korisnik_id):

    korisnik = Korisnik.objects.get(id=korisnik_id)
    context = {'korisnik': korisnik}

    return render(request, 'administracija/korisnik.html', context)




# pregled_projekata
# pregled_tehnologija
# pregled_kurseva
# pregled_postova
# pregled_korisnika