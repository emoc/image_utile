#!/usr/bin/python3

# afficher la liste des fichiers mp4 du dossier en cours
# pour en choisir un, interactivement
# créer un répertoire avec le nom du fichier
# extraire toutes les images de la vidéo dans ce dossier

# python 3.5.3
#   + pyyaml 3.12 ( pip3 show pyyaml )
#         * https://pyyaml.org/wiki/PyYAMLDocumentation
#   + argparse 1.4.0
#         * https://docs.python.org/3/library/argparse.html
#         * https://docs.python.org/fr/3/howto/argparse.html

import os
import sys
import argparse    # traitement des arguments de la ligne de commande
import yaml        # format utilisé pour le fichier de configuration


# Traitement des arguments en ligne de commande *******************************

parser = argparse.ArgumentParser(description="Test arguments et fichiers de configuration",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2], default=0, help="informations de debug")
parser.add_argument("-config", default="0", help="Fichier de configuration (yaml)")
args = parser.parse_args()

# Traitement du fichier de configuration si nécessaire ************************

if args.config != "0":
    if os.path.exists(args.config):
        with open(args.config, "r") as fp:
            args_yaml = yaml.safe_load(fp)
    else:
        print("le fichier " + args.config + " n'existe pas!");
        print("fin du script");
        exit()

# Traitement des valeurs récupérées dans l'étape de config

# *****************************************************************************

# Récupérer la liste des fichiers MP4 du dossier en cours
file_list = sorted([file for file in os.listdir('.') if file.endswith('.mp4')])

# Vérifier s'il y a des fichiers MP4 dans le dossier
if not file_list:
    print("Aucun fichier MP4 trouvé dans le dossier en cours.")
    sys.exit(1)

# Afficher la liste des fichiers MP4 avec des numéros
print("Liste des fichiers MP4 disponibles :")
for i, file in enumerate(file_list, 1):
    print("{}: {}".format(i, file))

# Lire le numéro du fichier sélectionné depuis l'entrée utilisateur
file_number = int(input("Entrez le numéro du fichier à traiter : "))

# Vérifier si le numéro de fichier sélectionné est valide
if file_number < 1 or file_number > len(file_list):
    print("Numéro de fichier invalide.")
    sys.exit(1)

# Extraire le nom de fichier correspondant au numéro sélectionné
selected_file = file_list[file_number - 1]

# Extraire le nom de fichier sans extension
dirname = os.path.splitext(selected_file)[0] + "_image_par_image"

# Créer le répertoire
os.mkdir(dirname)

# Copier le fichier dans le répertoire
#os.rename(selected_file, os.path.join(dirname, selected_file))

# Exécuter une commande sur le fichier (ici, un exemple avec la commande 'ls')
commande = "ffmpeg -i " + selected_file + " " + dirname + "/img_%04d.png"
os.system(commande)

# Changer le répertoire de travail vers le répertoire nouvellement créé
os.chdir(dirname)

os.system('ls')

# Revenir au répertoire précédent
os.chdir('..')

