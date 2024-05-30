from django.shortcuts import render, redirect, get_object_or_404
from .models import *

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