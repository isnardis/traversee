from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour accéder à l'interface d'administration Django
    path('', views.home, name='home'),  # URL pour la page d'accueil
    path('videos/', views.videos_view, name='videos'),  # URL pour la page des vidéos
    path('poemes/', views.poemes_view, name='poemes'),  # URL pour la page des poèmes
    path('memoire/', views.memoire, name='memoire'),  # URL pour la page du mémoire
    path('apropos/', views.apropos, name='apropos'),  # URL pour la page à propos
    ]
