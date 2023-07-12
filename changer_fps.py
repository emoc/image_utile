#!/usr/bin/python3

# Changer le fps d'une vidéo mp4 sans réencoder
#
# afficher la liste des fichiers mp4 du dossier en cours
# pour en choisir un, interactivement
# changer son nombre de frames per second (fps)
# le fichier de configuration optionnel n'est pas activé ici

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
import subprocess  # pour lancer une commande système en python 3.5

# Traitement des arguments en ligne de commande *******************************

parser = argparse.ArgumentParser(description="Changer le fps d'une vidéo mp4 sans réencoder",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2], default=0, help="informations de debug")
parser.add_argument("-config", default="0", help="Fichier de configuration (yaml)")
parser.add_argument("-fps", default="30", type=int, help="frames per second (fps)")
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

if args.fps != 30:
    newfps = args.fps
else:
    newfps = 30

# *****************************************************************************
print("newfps : ", newfps)


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

dest_file = os.path.splitext(selected_file)[0] + "_" + str(newfps) + "fps.mp4"
print(selected_file)
print(dest_file)

cmd1 = "ffmpeg -i " + selected_file + " -c copy -f h264 output_raw_bitstream.h264"
cmd2 = "ffmpeg -r " + str(newfps) + " -i output_raw_bitstream.h264 -c copy " + dest_file
cmd3 = "rm output_raw_bitstream.h264"

print("\n\n" + cmd1 + "\n")
subprocess.call(cmd1, shell=True)
print("\n\n" + cmd2 + "\n")
subprocess.call(cmd2, shell=True)
print("\n\n" + cmd3 + "\n")
subprocess.call(cmd3, shell=True)
