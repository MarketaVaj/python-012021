from django.db import models


class Auto(models.Model):
    registracniZnacka = models.CharField(max_length=7)
    pocetKilometru = models.IntegerField()
    datumKontroly = models.DateField()
    znackaTypVozidla = models.CharField(max_length=1000)
    def __str__(self):
        return self.znackaTypVozidla

class Zakaznik(models.Model):
    jmeno = models.CharField(max_length=20)
    prijmeni = models.CharField(max_length=20)
    cisloRidicskehoPRukazu = models.CharField(max_length=20)
    datumNarozeni = models.DateField()
    vypujcka = models.ForeignKey("Vypujcka", on_delete=models.SET_NULL, null=True)



class Vypujcka(models.Model):
    zacatekVypujcky = models.DateTimeField()
    konecVypujcky = models.DateTimeField()
    cenaVypujcky = models.IntegerField()
    auto = models.ForeignKey("Auto", on_delete=models.SET_NULL, null=True)
