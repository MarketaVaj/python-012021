
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from . import models

class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')

class KurzyView (ListView):
    model = models.Kurzy
    template_name = "kurzy/kurzy_list.html"