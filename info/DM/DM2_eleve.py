##EX 1 : Tracé d'une trajectoire d'usinage

import matplotlib.pyplot as plt   #pour le tracé de courbe
import numpy as np  #pour la définition de pi


# Paramètres
R1=70 #mm
k=6
e=6 #mm

R3=R1/k
R=R1-R3

R4=30 #mm

#Question 1 : liste discrétisée d'un angle

def liste_angle(n: int)->[]:
    '''retourne une liste de n éléments répartis uniformément entre 0 et 2*pi'''

    #A COMPLETER

    return()






#Question 2 : calcul des coordonnées de points de la trajectoire de C
def calcule_point_traj(a: float)-> (float, float):
    '''retourne les coordonnées d'un point C associé au paramètre a'''

    #A COMPLETER

    return()

#Question 3 : Tracé de la trajectoire du point C


#Question 5 : Fonction pour tracer un cercle de centre xc, yc et de rayon Rc
def trace_cercle(xc : float,yc : float,Rc : float)-> None:
    '''trace un cercle de centre C(xc,yc) et de rayon Rc'''
    a='rien'
    #A COMPLETER



#Question 6 : Tracé des différentes trajectoire d'un point de la fraise





##EX 2 : Repérage des alignements dans un jeu de puissance 4

#Définition des grilles de test
M1=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 3, 3, 3, 3, 1, 0],
[3, 1, 1, 1, 3, 1, 0],
[1, 3, 1, 3, 3, 1, 0]]

M2=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 3, 3],
[0, 0, 0, 3, 1, 3, 1],
[0, 0, 3, 1, 1, 1, 3]]

M3=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 3, 0, 0, 0, 0],
[0, 0, 3, 3, 0, 0, 0],
[0, 0, 3, 1, 1, 1, 0],
[0, 1, 3, 1, 1, 3, 0],
[0, 3, 1, 1, 3, 3, 1]]

M4=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 3, 0, 0, 0],
[0, 0, 3, 3, 3, 1, 0],
[0, 0, 3, 1, 1, 3, 1],
[0, 0, 3, 1, 1, 1, 3]]

M5=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 3, 3, 1, 3, 0, 0],
[0, 1, 1, 3, 1, 0, 0],
[0, 1, 3, 1, 3, 0, 0]]

M6=[
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0],
[0, 1, 1, 3, 3, 0, 0],
[1, 3, 3, 3, 1, 3, 0],
[3, 3, 1, 1, 1, 3, 0],
[1, 3, 3, 1, 1, 1, 0]]

#Question 6



#Question 7 : Test
def quatre_a_la_suite_horizontal(grille : [[int]], c: int)->bool:
    """ décèle un alignement horizontal de 4 pions de même couleur (c est l'entier associé à la couleur)
    entrée : grille, un tableau d'au moins 4 colonnes
    sortie : True si 4 pions de même couleur sont alignés horizontalement
             False sinon
    """
    rep = False
    for i in range(6): # boucle sur les 6 lignes
        for j in range(4): #boucle les colonnes, teste sur les 4 premières colonnes
            if grille[i][j] == c and grille[i][j+1] == c and grille[i][j+2] == c and grille[i][j+3] == c:
                rep = True

    return(rep)

#tests (sous forme de commentaires)



#Question 8
def quatre_a_la_suite_vertical(grille : [[int]], c: int)->bool:
    """ décèle un alignement vertical de 4 pions de même couleur (c est l'entier associé à la couleur)
    entrée : grille, un tableau d'au moins 4 lignes
    sortie : True si 4 pions de même couleur sont alignés verticalement
             False sinon
    """

    return()
#tests (sous forme de commentaires)


#Question 9

def quatre_a_la_suite_oblique(grille : [[int]], c: int)->bool:
    """ décèle un alignement oblique de 4 pions de même couleur (c est l'entier associé à la couleur)
    entrée : grille
    sortie : True si 4 pions de même couleur sont alignés
             False sinon
    """

    return()

#tests (sous forme de commentaires)

