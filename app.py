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
px.load("datas.pyxres")


# initialisation des tirs
tirs_liste = []

# init des rochers
rochersListL = [[5, 210], [20, 210], [60, 210], [95, 210], [95, 228], [95, 243]]
rocherListB = []

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
        if (y < 238):
            y = y + 1
    return x, y


def tirs_creation(x,y,tirs_liste):
    if px.btnr(px.MOUSE_BUTTON_LEFT) or px.btnr(px.KEY_SPACE):
        tirs_liste.append([x+8, y-4])
    return tirs_liste

def tirs_deplacement(tirs_liste):
    for tir in tirs_liste:
        tir[1] -= 1
        if  tir[1]<-8:
            tirs_liste.remove(tir)
    return tirs_liste

"""def rochersL_creation(x, y):
    global rochersListL
    rochersListL.append([x, y])

def rochersL_creation(x, y):"""


#################### VOID UPDATE ####################
def update():
    global perso_x, perso_y, perso_x, perso_y, tirs_liste
    perso_x, perso_y = deplacement_perso(perso_x, perso_y)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(perso_x, perso_y, tirs_liste)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)


##################### VOID DRAW #####################

def draw():
    #Fond rouge
    px.cls(4)

    #Draw le personnage
    #px.rect(perso_x, perso_y, 16, 16, 8)
    #blt(x, y, img, u, v, w, h, [colkey])
    #Copie la région de taille (w, h) de (u, v) de la banque d’image img(0-2) à (x, y).
    #Si une valeur négative est mise pour w(ou h), la copie sera inversée horizontalement 
    #(ou verticalement). Si colkey est spécifiée, elle sera traitée comme une couleur transparente.

    px.blt(perso_x, perso_y, 0, 0, 8, 16, 15, 5)

    #Draw le décor (rochers)
    #Rochers simples
    """px.blt(5, 210, 0, 176, 128, 16, 15, 5)
    px.blt(20, 210, 0, 176, 128, 16, 15, 5)
    px.blt(60, 210, 0, 176, 128, 16, 15, 5)
    px.blt(95, 228, 0, 176, 128, 16, 15, 5)
    px.blt(95, 243, 0, 176, 128, 16, 15, 5)"""
    for rocherL in rochersListL:
        px.blt(rocherL[0], rocherL[1], 0, 176, 128, 16, 15, 5)


    #Rochers 3x16
    px.blt(75, 210, 0, 224, 128, 3*16, 16, 5)

    # tirs
    for tir in tirs_liste:
        px.rect(tir[0], tir[1], 1, 4, 10)





##################### EXECUTION DU CODE #####################
px.run(update, draw)
