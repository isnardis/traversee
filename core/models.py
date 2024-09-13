from django.db import models

class Video(models.Model):
    LANGUES = [
        ('fr', 'Français'),
        ('pt', 'Portugais'),
        ('bi', 'Bilingue'),
    ]

    LIEUX = [
        ('int', 'Intérieur'),
        ('ext', 'Extérieur'),
    ]

    titre = models.CharField(max_length=200)  # Champ pour le titre de la vidéo
    description = models.TextField()  # Champ pour la description de la vidéo
    langue = models.CharField(max_length=2, choices=LANGUES)  # Champ pour la langue de la vidéo
    lieu = models.CharField(max_length=3, choices=LIEUX)  # Champ pour le lieu de tournage de la vidéo
    musique = models.BooleanField(default=False)  # Champ booléen indiquant si la vidéo contient de la musique
    fichier = models.FileField(upload_to='videos/')  # Champ pour le fichier vidéo à télécharger

    def __str__(self):
        return self.titre  # Retourne le titre de la vidéo comme représentation en chaîne de caractères

class Poeme(models.Model):
    LANGUES = [
        ('fr', 'Français'),
        ('pt', 'Portugais'),
        ('bi', 'Bilingue'),
    ]

    titre = models.CharField(max_length=200)  # Champ pour le titre du poème
    contenu = models.TextField()  # Champ pour le texte du poème
    langue = models.CharField(max_length=2, choices=LANGUES)  # Champ pour la langue du poème
    auteur = models.CharField(max_length=200) #Champ pour l'auteur du poème
    def __str__(self):
        return self.titre  # Retourne le titre du poème comme représentation en chaîne de caractères

