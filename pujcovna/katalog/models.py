from django.db import models


class Auto(models.Model):
    registracniZnacka = models.CharField(max_length=7)
    pocetKilometru = models.IntegerField()
    datumKontroly = models.DateField()
    znackaTypVozidla = models.CharField(max_length=1000)


class Zakaznik(models.Model):
    Jmeno = models.CharField(max_length=20)
    Prijmeni = models.CharField(max_length=20)
    CisloRidicskehoPRukazu = models.CharField(max_length=20)
    datumNarozeni = models.DateField()

class Vypujcka(models.Model):
  ZacatekVypujcky = models.DateTimeField()
  KonecVypujcky = models.DateTimeField()
  CenaVypujcky = models.IntegerField()