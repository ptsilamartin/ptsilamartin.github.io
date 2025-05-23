# -*- coding: utf-8 -*-
import time

from collections import deque
import matplotlib.pyplot as plt
import random

def creer_graphe(n:int, p:int) -> dict:
    '''créer le graphe d’une grille de n colonnes et p lignes'''
    G = {}
    sommets = []
    for i in range(p):
        for j in range(n):
            sommets.append((i,j))
    
    for sommet in sommets : 
        (i,j) = sommet
        voisins = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
        # On vérifie que les voisins sont dans les sommets
        vv = []
        for v in voisins : 
            if v in sommets : 
                vv.append(v)
        G[sommet]=vv
    return G

def get_sommets(G:{}) -> ([],[]):
    '''fonction renvoyant deux listes les_x et les_y contenant respectivement les abscisses des sommets et les ordonnées des sommets.'''
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[1])
        les_y.append(sommet[0])
    return les_x,les_y
                
def trace_sommets(G:dict,couleur:int)->None:
    '''trace sur la figure courante les sommets du graphe G en utilisant un point coloré de la couleur spécifiée:
    pour avoir les sommets en rouge : couleur prend la valeur "r" 
    pour avoir les sommets en noir : couleur prend la valeur "k" '''
    les_x,les_y=get_sommets(G)
    plt.plot(les_x,les_y,couleur+'.')
    plt.axis('equal')
 
def get_aretes(G):
    '''fonction renvoyant la liste des arêtes du graphe G sous la forme d’une liste de listes de tuples
    exemple :[[(0, 0), (1, 0)], [(0, 0), (0, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 1)]]'''
    edges = []
    for sommet,voisins in G.items():
        for v in voisins : 
            edge = [sommet,v]
            if [sommet,v] not in edges : 
                if [v,sommet] not in edges : 
                    edges.append(edge)
    return edges

def trace_arete(s1,s2,couleur,epaisseur)->None:
    '''trace une arête reliant les sommets s1 et s2 sur la figure courante
    couleur prend la valeur 'r' pour le rouge, 'b' pour du bleu, 'k' pour du noir
    l'épaisseur est un flottant : 1 est une épaisseur standard pour le TP'''
    les_x = [s1[1],s2[1]]
    les_y = [s1[0],s2[0]]
    plt.plot(les_x,les_y,couleur,linewidth=epaisseur)
 
    
def trace_graphe(G:dict,couleur:str,epaisseur:int)->None:
    '''trace les sommets et les arêtes du graphe G sur la figure courante'''
    aretes=get_aretes(G)
    for a in aretes :
        trace_arete(a[0],a[1],couleur,epaisseur)
    trace_sommets(G,couleur)


def ajouter_arete(L:dict,s1:tuple,s2:tuple):
    '''ajoute l'arrete (s1,s2) au graphe L, si elle n'existe pas déjà'''
    if (s1 not in L.keys()) :  # si s1 n'existe pas
        L[s1]=[s2]
    if (s2 not in L.keys()):
        L[s2]=[s1]

    if s2 not in L[s1] : #si s2 n'est pas dans les voisins de s1
         L[s1].append(s2)
    if s1 not in L[s2] :
         L[s2].append(s1)

def trace_visites(visites:dict):
    '''réalise le tracé sur la figure courante du dictionnaire visites suivant les régles suivantes :
    les clés de ce dictionnaires sont les coordonnées du point (noeud) considéré sous la forme d'un tuple (i,j)
    i - entier pour l'ordonnée ; j : entier pour l'abcisse 
    si la valeur est 'G' le noeud est coloré en gris
    si le valeur est 'K' le noeud est coloré en noir'''
    for e in visites.keys():
         if visites[e]=='G':
                plt.plot(e[1],e[0],'o',color='grey',markersize=8)  #Tracé des éléments 'G' en gris
         if visites[e]=='K':
             plt.plot(e[1],e[0],'ko',markersize=8)  #Tracé des éléments 'K' en noir

## Préambule : utilisation des fonctions fournies
plt.figure("Tracé 1")
G1=creer_graphe(4,3)  #Crée un graphe de 4 colonnes et 3 lignes
trace_graphe(G1,'r',1) #trace

print(G1) #affichage dans le shell du dictionnaire d'adjacence du graphe G1


#Question 1 : ajout de l'arete (0,0) ; (1,1) au graphe G ; affichage dans une figure nommée "tracé 2"    

''' A compléter '''


#Question 2 : créer le dictionnaire de marquage

''' A compléter '''

#Question 3    
#affectation arbitraire du sommet en haut à gauche en gris
''' A compléter '''

#affectation arbitraire du sommet en haut à droite en noir
''' A compléter '''

#Affichage
''' A compléter '''


##Patie 3 Création du labyrinthe par un parcours en parcours en largeur
#Création du graphe à parcourir
G=creer_graphe(10,8)  #Crée un graphe de 10 colonnes et 8 lignes


#Question 4 : initialisation
def parcours_largeur_init(G:{},depart:tuple) :
    #Initialisation du dictionnaire des noeuds visites
    ''' A compléter '''
    
    
    #Initialisation de la file : file ne contenant que le sommet de départ
    ''' A compléter '''
    
    #Initialisation du labyrinthe : dictionnaire vide
    ''' A compléter '''
    
    #Modification de l'état du sommet de départ comme "découvert" en modifiant le dictionnaire des sommets visites
    ''' A compléter '''
    #Tracé du dictionnaire obtenu
    trace_visites(visited)

# plt.figure("largeur_initial")
# trace_graphe(G,'r',1) #trace
# parcours_largeur_init(G,(0,0))
 
#Question 5 : parcours en largeur : etape 1
def parcours_largeur_etape1(G:{},depart:tuple) :
    #Initialisations
    ''' A compléter en recopiant ce qui a été fait précédemment'''
    
    #Première étape d'exploration
    '''A completer'''
    
    #Tracé du dictionnaire obtenu
    trace_visites(visited)
     
# plt.figure("largeur_étape1")
# trace_graphe(G,'r',1)
# parcours_largeur_etape1(G,(0,0))
 
#Question 6 : parcours en largeur complet

def parcours_largeur_laby(G:{},depart: tuple) :
    #Initialisation du dictionnaire des noeuds visites
    ''' A compléter en recopiant ce qui a été fait précédemment'''
    
    #Exploration en largeur
    while rien=='rien' : #Compléter la condition d'arrêt
         
        ''' a completer'''
         
         
         
        plt.pause(0.5)
        #print(file)
        trace_visites(visited)
        trace_graphe(labyrinthe,'k',3)
    return(labyrinthe)
     
# plt.figure("labyrinthe en largeur")
# trace_graphe(G,'r',1)
# parcours_largeur_laby(G,(0,0))
   
##Partie 4 : création du labyrinthe par parcours en profondeur
 
#Question 7 : 

def parcours_profondeur_laby(G:{},depart:tuple) :
    #initialisation
    '''a completer'''
    while rien=='rien' : #Compléter la condition d'arrêt
            rien='rien'
        
        
    return(labyrinthe) 
    
# plt.figure("labyrinthe en profondeur")
# trace_graphe(G,'r',1)
# parcours_profondeur_laby(G,(0,0))
 
##Partie 5 : résolution du labyrinthe




plt.show()