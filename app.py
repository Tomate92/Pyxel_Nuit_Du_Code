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

perso_x = 0
perso_y = 256


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
        x += 1
    if px.btn(px.KEY_LEFT):
        x += -1
    if px.btn(px.KEY_UP):
        y += 1
    if px.btn(px.KEY_DOWN):
        y += -1


#################### VOID UPDATE ####################
def update():
    global perso_x, perso_y
    perso_x, perso_y = deplacement_perso(perso_x, perso_y)







##################### VOID DRAW #####################

def draw():
    px.cls(0)
    px.rect(perso_x, perso_y, 16, 16, 1)


##################### EXECUTION DU CODE #####################
px.run(update, draw)
