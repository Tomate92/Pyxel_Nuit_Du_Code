# Installer un module python sur VSCode : taper "py -m pip install [nom du module]" dans le terminal 
# Pour éditer le fichier audio/graphiques (.pyxres), taper "py -m pyxel edit [PYXEL_RESOURCE_FILE]" dans la console
# (Remplacer [PYXEL_RESOURCE_FILE] par le nom voulu, peu importe)
# ATTENTION : cette ligne s'exécute dans le dossier courant (pour naviguer dans les dossiers, utiliser la cmd "cd")
# Docu officielle de Pyxel : https://github.com/kitao/pyxel/blob/main/docs/README.fr.md#comment-cr%C3%A9er-une-ressource
# Installer Pyxel en portable en local (très pratique à l'école car on a pas les droits admin) : https://nuit-du-code.forge.apps.education.fr/DOCUMENTATION/05-materiel-logiciels#python-pyxel_1

# Copyright © 2024 GauGoth Corp. All rights reserved - http://gaugoth.corp.free.fr
import pyxel as px
import random  

##################### INITIALISATION #####################

# taille de la fenetre 128x128 pixels OU 256x256
# /!\ ne pas modifier => taille obligatoire pour le concours
px.init(256, 256, title="Test")

# chargement des ressources
px.load("3.pyxres")



#####################################################
##################### Variables #####################
#####################################################

perso_x = 7
perso_y = 236


#####################################################
##################### FONCTIONS #####################
#####################################################




#####################################################
##################### PROGRAMME #####################
#####################################################

def deplacement_perso(x,y):
    if px.btnp(px.KEY_ESCAPE):
        px.quit
    if px.btn(px.KEY_RIGHT):
        if (x < 248):
            x = x + 1
    if px.btn(px.KEY_LEFT):
        if (x > 0):
            x = x - 1
    if px.btn(px.KEY_UP):
        if (y > 0):
            y = y - 1
    if px.btn(px.KEY_DOWN):
        if (y < 248):
            y = y + 1
    return x, y


#################### VOID UPDATE ####################
def update():
    global perso_x, perso_y
    perso_x, perso_y = deplacement_perso(perso_x, perso_y)







##################### VOID DRAW #####################

def draw():
    px.cls(0)
    px.rect(perso_x, perso_y, 16, 16, 8)
    px.blt(60, 60, 0, 176, 128, 16, 15, 5)
    px.blt(75, 60, 0, 176, 128, 16, 15, 5)
    px.blt(90, 60, 0, 176, 128, 16, 15, 5)
    px.blt(105, 60, 0, 176, 128, 16, 15, 5)
    px.blt(120, 60, 0, 176, 128, 16, 15, 5)



##################### EXECUTION DU CODE #####################
px.run(update, draw)
