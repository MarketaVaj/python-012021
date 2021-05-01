from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

class MujDruhyPohled(View):
    def get(self, request):
        return HttpResponse('Vítej v CRM systému Czechitas!')