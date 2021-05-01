from django.shortcuts import render

from django.views import View
from django.http import HttpResponse

class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')