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

#####################################################
##################### Variables #####################
#####################################################

perso_x = 7
perso_y = 236

#Init time
temps = 0

# persoAuthMouv = True

ennemis_liste = []

# initialisation des tirs
tirs_liste = []

# init des rochers
rochersListL = [[5, 210], [5, 190], [5, 175], [20, 175], [20, 210], [60, 210], [95, 210], [95, 228], [95, 243],
                [60, 60], [75, 60], [75, 77], [58, 75], [120, 55], [120, 125], [142, 126], [158, 126], [178, 131],
                [180, 205], [195, 205], [183, 35], [201, 36]]
rocherListB = []

perso_pos = '1'

vies = 4
kill = 0

# initialisation des explosions
explosions_liste = []


#####################################################
##################### FONCTIONS #####################
#####################################################


def deplacement_perso(x, y):
    global rochersListL, perso_x, perso_y, perso_pos  # , persoAuthMouv
    x2, y2 = x, y
    if px.btn(px.KEY_RIGHT):
        if (x < 248):
            x2 = x + 3
            perso_pos = '1'
    if px.btn(px.KEY_LEFT):
        if (x > 0):
            x2 = x - 3
            perso_pos = '2'
    if px.btn(px.KEY_DOWN):
        if (y < 248):
            y2 = y + 3
    if px.btn(px.KEY_UP):
        if (y > 0):
            y2 = y - 3

    for rocher in rochersListL:  # Si joueur trop proche rocher, on change pas les x,y
        if rocher[0] - 17 < x2 < rocher[0] + 14 and rocher[1] - 14 < y2 < rocher[1] + 15:
            return x, y, perso_pos
    return x2, y2, perso_pos


def ennemis_deplacement(ennemis_liste, x_du_perso, y_du_perso):
    for ennemi in ennemis_liste:
        if x_du_perso > ennemi[0]:
            ennemi[0] += ennemi[3]
            ennemi[2] = '2'
        if x_du_perso < ennemi[0]:
            ennemi[0] -= ennemi[3]
            ennemi[2] = '1'
        if y_du_perso > ennemi[1]:
            ennemi[1] += ennemi[3]
        if y_du_perso < ennemi[1]:
            ennemi[1] -= ennemi[3]
    return ennemis_liste


def ennemis_creation(ennemis_liste, x_du_perso):
    x_ennemi = random.randint(0, 256)
    y_ennemi = random.randint(0, 256)
    vitesse_ennemi = random.randint(50, 150) / 100

    if x_du_perso > x_ennemi:
        position = '2'
    if x_du_perso < x_ennemi:
        position = '1'
    # un ennemi par seconde
    if (px.frame_count % 60 == 0):
        ennemis_liste.append([x_ennemi, y_ennemi, position, vitesse_ennemi])
    return ennemis_liste


def tirs_creation(x, y, tirs_liste, perso_pos):
    if px.btnr(px.MOUSE_BUTTON_LEFT) or px.btnr(px.KEY_SPACE):
        px.play(0,0)
        if perso_pos == '1':
            tirs_liste.append([x + 16, y + 3, perso_pos])
        elif perso_pos == '2':
            tirs_liste.append([x - 16, y + 3, perso_pos])
    return tirs_liste


def tirs_deplacement(tirs_liste):
    for tir in tirs_liste:
        if tir[2] == '1':
            tir[0] += 1
        elif tir[2] == '2':
            tir[0] += -1
        if tir[0] > 270 or tir[0] < -5:
            tirs_liste.remove(tir)

    return tirs_liste


"""def rochersL_colisions(x, y):
    global rochersListL, perso_x, perso_y, persoAuthMouv

    persoAuthMouv = True

    for rocher in rochersListL:
        if rocher[0] <= perso_x+15 and rocher[1] <= perso_y+15 and rocher[0]+8 >= perso_x and rocher[1]+8 >= perso_y:
            persoAuthMouv = False"""


def enemi_delet(vies):
    for ennemi in ennemis_liste:
        if ennemi[0] <= perso_x + 8 and ennemi[1] <= perso_y + 8 and ennemi[0] + 8 >= perso_x and ennemi[
            1] + 8 >= perso_y:
            ennemis_liste.remove(ennemi)
            vies -= 1
    return vies


def ennemis_suppression():
    global kill

    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0] + 1 and ennemi[0] + 8 >= tir[0] and ennemi[1] + 8 >= tir[1]:
                ennemis_liste.remove(ennemi)
                try:
                    tirs_liste.remove(tir)
                except ValueError:
                    pass
                explosions_creation(ennemi[0], ennemi[1])
                kill += 1
                px.play(1, 1)
    return ennemis_liste


def explosions_creation(x, y):
    explosions_liste.append([x, y, 0])


def explosions_animation():
    for explosion in explosions_liste:
        explosion[2] += 1
        if explosion[2] == 23:
            explosions_liste.remove(explosion)


#####################################################
##################### PROGRAMME #####################
#####################################################

#################### VOID UPDATE ####################
def update():
    global perso_x, perso_y, ennemis_liste, tirs_liste, vies, perso_pos
    if px.frame_count == 0:
        px.playm(0, 20, True)

    perso_x, perso_y, perso_pos = deplacement_perso(perso_x, perso_y)
    ennemis_liste = ennemis_deplacement(ennemis_liste, perso_x, perso_y)
    ennemis_liste = ennemis_creation(ennemis_liste, perso_x)

    # creation des tirs en fonction de la position du vaisseau
    tirs_liste = tirs_creation(perso_x, perso_y, tirs_liste, perso_pos)

    # mise a jour des positions des tirs
    tirs_liste = tirs_deplacement(tirs_liste)

    ennemis_liste = ennemis_suppression()
    vies = enemi_delet(vies)
    explosions_animation()


##################### VOID DRAW #####################

def draw():
    global perso_pos, perso_x, perso_y, vies, kill, temps
    # Fond rouge
    px.cls(4)

    # Draw le personnage
    # px.rect(perso_x, perso_y, 16, 16, 8)
    # blt(x, y, img, u, v, w, h, [colkey])
    # Copie la région de taille (w, h) de (u, v) de la banque d’image img(0-2) à (x, y).
    # Si une valeur négative est mise pour w(ou h), la copie sera inversée horizontalement
    # (ou verticalement). Si colkey est spécifiée, elle sera traitée comme une couleur transparente.
    if perso_pos == '1':
        px.blt(perso_x, perso_y, 0, 0, 8, 16, 15, 5)
    elif perso_pos == '2':
        px.blt(perso_x, perso_y, 0, 0, 8, -16, 15, 5)

    # Draw le décor (rochers)
    # Rochers simples
    for rocherL in rochersListL:
        px.blt(rocherL[0], rocherL[1], 0, 176, 128, 16, 15, 5)


    if vies > 0:
        #Affiche le temps
        if px.frame_count % 30 == 0:
            temps += 1
            px.text(120, 10, str(temps) + 's', 7)
        else:
            px.text(120, 10, str(temps) + 's', 7)

        px.blt(5, 5, 0, 48, 216, 16, 16, 5)
        px.text(25, 10, str(vies), 7)
        px.blt(235, 5, 0, 32, 216, 16, 16, 5)
        px.text(225, 10, str(kill), 7)

        # tirs
        for tir in tirs_liste:
            px.blt(tir[0], tir[1], 0, 48, 8, 7, 7, 5)

        for ennemi in ennemis_liste:
            if ennemi[2] == '2':
                px.blt(ennemi[0], ennemi[1], 0, 0, 120, 16, 16, 5)
            if ennemi[2] == '1':
                px.blt(ennemi[0], ennemi[1], 0, 0, 120, -16, 16, 5)
        for explosion in explosions_liste:
            px.circb(explosion[0] + 4, explosion[1] + 4, 2 * (explosion[2] // 4), 8 + explosion[2] % 3)
    else:
        px.cls(0)

        px.text(107, 110, 'GAME OVER', 7)
        px.text(100, 158, 'Vous avez survecu ' + str(temps) + "s !", 3)
        px.blt(110, 128, 0, 32, 184, 16, 16, 5)
        px.text(130, 133, str(kill), 7)
        if (px.frame_count % 120 == 0):
            px.quit()

    #  tirs


##################### EXECUTION DU CODE #####################
px.run(update, draw)