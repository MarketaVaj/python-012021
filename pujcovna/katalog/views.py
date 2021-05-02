from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

class indexView(View):
     def get(self, request):
         return HttpResponse("Zde bude titulní stránka.")

# class indexView(View):
#     def get(self, request):
#         return HttpResponse("<a href='http://localhost:8000/katalog/seznam/'>Katalog</a>")

# class indexView(View):
#     def get(self, request):
#         return HttpResponse("<h1>Vítejte v naší autopůjčovně!</h1>")

class seznamView(View):
    def get(self, request):
         return HttpResponse('Zde bude seznam aut.')

