#!/usr/bin/python3

# python 3.5.3

import glob
import os

# Chemin du dossier contenant les fichiers MP4 (chemin actuel)
dossier_mp4 = os.getcwd()

# Chemin du fichier de playlist M3U à créer
fichier_playlist = os.path.join(dossier_mp4, 'playlist.m3u')

# Recherche des fichiers MP4 dans le dossier spécifié
fichiers_mp4 = glob.glob(os.path.join(dossier_mp4, '*.mp4'))

# Obtention des chemins relatifs des fichiers MP4
fichiers_rel = [os.path.relpath(fichier, dossier_mp4) for fichier in fichiers_mp4]

# Tri des chemins relatifs par ordre alphabétique
fichiers_rel = sorted(fichiers_rel)

# Écriture des noms de fichiers dans le fichier de playlist M3U
with open(fichier_playlist, 'w') as playlist:
    for fichier_rel in fichiers_rel:
        playlist.write(fichier_rel + '\n')


print("Playlist M3U créée avec succès.")
