from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("vypujcka", views.VypujckaView.as_view(), name="vypujcka"),
    path("auto", views.AutoView.as_view(), name="auto"),
    path("zakaznik", views.ZakaznikView.as_view(), name="zakaznik")
]



