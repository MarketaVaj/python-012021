from django.db import models

class Kontakt(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  datum_posledniho_kontaktu = models.DateTimeField()
