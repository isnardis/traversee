from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Poeme, Video


def poemes_view(request):
    # Récupérer les paramètres de filtrage depuis la requête GET
    langue = request.GET.get('langue', '')  # Par défaut vide
    auteur = request.GET.get('auteur', '')  # Par défaut vide

    # Appliquer le filtrage sur les poèmes si les critères sont définis
    poemes = Poeme.objects.all()
    if langue:
        poemes = poemes.filter(langue=langue)
    if auteur:
        poemes = poemes.filter(auteur__icontains=auteur)

    # Pagination (2 poèmes par page)
    paginator = Paginator(poemes, 2)
    page_number = request.GET.get('page')
    
    # S'assuer que le nombre de pages est valide
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'core/poemes.html', {
        'page_obj': page_obj,
        'langue': langue,
        'auteur': auteur
    })



# View pour la page de vidèos
def videos_view(request):
    langue = request.GET.get('langue')
    lieu = request.GET.get('lieu')
    musique = request.GET.get('musique')

    # Filtres
    videos = Video.objects.all()
    if langue:
        videos = videos.filter(langue=langue)
    if lieu:
        videos = videos.filter(lieu=lieu)
    if musique:
        videos = videos.filter(musique=musique)

    # Pages : 5 vidèos par page
    paginator = Paginator(videos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'core/videos.html', {'page_obj': page_obj, 'langue': langue, 'lieu': lieu, 'musique': musique})

# View pour la home page
def home(request):
    return render(request, 'core/home.html')

# View pour la page du mémoire
def memoire(request):
    return render(request, 'core/memoire.html')

# View pour la page À propos
def apropos(request):
    return render(request, 'core/apropos.html')
