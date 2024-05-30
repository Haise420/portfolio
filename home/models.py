from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Korisnik(models.Model):
    ime = models.OneToOneField(User, on_delete=models.CASCADE)
    pretplata = models.BooleanField(default=False)

    def __str__(self):
        return self.ime.username


class Projekat(models.Model):
    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    datum_pocetka = models.DateField()
    datum_zavrsetka = models.DateField(null=True, blank=True)
    tehnologije = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)
    slika = models.ImageField(upload_to='projekti/', null=True, blank=True)
    pretplata = models.BooleanField(default=False)
    
    def __str__(self):
        return self.naziv

class Kurs(models.Model):
    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    platforma = models.CharField(max_length=255)
    datum_pocetka = models.DateField()
    datum_zavrsetka = models.DateField(null=True, blank=True)
    sertifikat = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.naziv


class Level(models.Model):
    kurs = models.ForeignKey(Kurs, related_name='levele', on_delete=models.CASCADE)
    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    video_url = models.URLField()
    redni_broj = models.IntegerField()
    
    class Meta:
        unique_together = ('kurs', 'redni_broj')
        ordering = ['redni_broj']
    
    def __str__(self):
        return f"{self.kurs.naziv} - {self.naziv}"
    

class Post(models.Model):
    naslov = models.CharField(max_length=40)
    text = models.TextField(max_length=12000)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    kreirao = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    kreiran = models.DateTimeField(auto_now_add=True)
    slika = models.ImageField(upload_to='postovi/', null=True, blank=True)

    def __str__(self):
        return f"{self.naslov} - {self.kreiran}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.naslov)
        super().save(*args, **kwargs)