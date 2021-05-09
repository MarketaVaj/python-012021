from django.shortcuts import render

from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from . import models

class IndexView(View):
     def get(self, request):
         return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>
<a href='http://localhost:8000/auto'>Jaká auta máme?</a><br>
<h2>O naší autopůjčovně</h2>
<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
""")

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>")

# class IndexView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Vítejte v naší autopůjčovně!</h1>")


class VypujckaView (ListView):
    template_name = "vypujcka.html"
    model = models.Vypujcka

class AutoView (ListView):
    template_name = "seznam.html"
    model = models.Auto

class ZakaznikView (ListView):
    template_name = "zakaznik.html"
    model = models.Zakaznik
