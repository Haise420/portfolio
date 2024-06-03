from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Korisnik(models.Model):
    ime = models.OneToOneField(User, on_delete=models.CASCADE)
    pretplata = models.BooleanField(default=False)
    slika = models.ImageField(upload_to='korisnici/slike', blank=True)

    def __str__(self):
        return self.ime.username
    
class Tehnologija(models.Model):
    ime = models.CharField(max_length=255)
    slika = models.ImageField(upload_to='tehnologije/')

    def __str__(self):
        return self.ime


class Projekat(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    VERSION_STAGE_CHOICES = [
        ('Alpha', 'Alpha'),
        ('Beta', 'Beta'),
        ('Release Candidate (RC)', 'Release Candidate (RC)'),
        ('Stable/General Availability (GA)', 'Stable/General Availability (GA)'),
    ]


    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    datum_pocetka = models.DateField()
    datum_zavrsetka = models.DateField(null=True, blank=True)
    tehnologije = models.ManyToManyField(Tehnologija)
    link = models.URLField(null=True, blank=True)

    tezina = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='Easy')
    verzija_stage = models.CharField(max_length=32, choices=VERSION_STAGE_CHOICES, default='Alpha')
    verzija = models.CharField(max_length=20, blank=True)

    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.naziv
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.naziv)
        super().save(*args, **kwargs)



class SlikeProjekta(models.Model):
    projekat = models.ForeignKey('Projekat', related_name='slike', on_delete=models.CASCADE)
    slika = models.ImageField(upload_to='projekti/slike/')
    
    def __str__(self):
        return f"Slika za {self.projekat.naziv}"

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