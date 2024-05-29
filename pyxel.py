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
    if px.btn(px.RIGHT):
        x += 1
    if px.btn(px.LEFT):
        x += -1
    if px.btn(px.UP):
        y += 1
    if px.btn(px.DOWN):
        y += -1


#################### VOID UPDATE ####################
def update():
    global perso_x, perso_y
    perso_x, perso_y = deplacement_perso(perso_x, perso_y)







##################### VOID DRAW #####################

def draw():
    pass

##################### EXECUTION DU CODE #####################
px.run(update, draw)
