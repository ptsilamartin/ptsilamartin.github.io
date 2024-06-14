# -*- coding: utf-8 -*-
import time

from collections import deque
import matplotlib.pyplot as plt
import random


##########TP : partie préliminaire

## Question 1 ##
def creer_graphe(p:int, n:int) -> dict:
    # n : lignes
    # p : colonnes
    G = {}
    sommets = []
    for i in range(n):
        for j in range(p):
            sommets.append((j,i))
    
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

## Question 2 ##
def get_sommets(G:{}) -> ([],[]):
    # On trace les sommets
    les_x,les_y = [],[]
    for sommet in G.keys() : 
        les_x.append(sommet[0])
        les_y.append(sommet[1])
    return les_x,les_y
                
### question 3 ##
def trace_sommets(G:dict,couleur:int)->None:
    les_x,les_y=get_sommets(G)
    plt.plot(les_x,les_y,couleur+'.')
    plt.axis('equal')
 
    
    
## Question 4 ##
def get_aretes(G):
    edges = []
    for sommet,voisins in G.items():
        for v in voisins : 
            edge = [sommet,v]
            if [sommet,v] not in edges : 
                if [v,sommet] not in edges : 
                    edges.append(edge)
    return edges


## Question 5 ##  
def trace_arete(s1,s2,couleur,epaisseur)->None:
    les_x = [s1[0],s2[0]]
    les_y = [s1[1],s2[1]]
    plt.plot(les_x,les_y,couleur,linewidth=epaisseur)

    

## Question 6 ##
def trace_graphe(G:dict,couleur:str,epaisseur:int)->None:
    aretes=get_aretes(G)
    for a in aretes :
        trace_arete(a[0],a[1],couleur,epaisseur)
    trace_sommets(G,couleur)



# 
##########TP
def ajouter_arete(G,s1,s2):
    if s1 in G : 
        G[s1].append(s2)
    else : 
        G[s1]=[s2]
    
    if s2 in G : 
        G[s2].append(s1)
    else : 
        G[s2]=[s1]
# 
# G=creer_graphe(10,8)
# 
# ajouter_arete(G,(11,11),(12,12))
# ajouter_arete(G,(0,0),(1,1))
# 
# ajouter_arete(G,(6,6),(4,14))
# trace_graphe(G,'r',1)
# # plt.show()
def trace_visite(v):
    for s,couleur in v.items() :
        if couleur == "G":
            plt.plot(s[0],s[1],'o',color='grey')
        elif couleur == "K" :
            plt.plot(s[0],s[1],'o',color='black')

def parcours_largeur_complet(G,dep):
    file = deque([dep])
    laby = {}
    #Initialisation v
    visited = {}
    for s in G.keys() : 
        visited[s] = "W"
    visited[dep] = "G"

    while len(file) != 0 :
        s = file.pop()
        voisins = G[s]
        random.shuffle(voisins)
        for v in voisins : 
            if visited[v] == "W" :
                file.appendleft(v)
                trace_arete(s,v,'k',3)
                visited[v] = "G"
                ajouter_arete(laby,s,v)
                
                
        visited[s] = "K"
        plt.pause(0.3)
        trace_visite(visited)
    return laby
    
    
# Animation (parcours en largeur)
# plt.figure("largeur")
# G=creer_graphe(10,8)
# trace_graphe(G,'r',.5)
# laby = parcours_largeur_complet(G,(4,4))
# trace_graphe(laby,'k',2)
# plt.show()  
#     
    
#     
#     
def parcours_profondeur(G,dep):
    file = deque([dep])
    laby = {}
    #Initialisation v
    visited = {}
    for s in G.keys() : 
        visited[s] = "W"
    visited[dep] = "G"

    while len(file) != 0 :
        s = file.pop()
        voisins = G[s]
        random.shuffle(voisins)
        for v in voisins : 
            if visited[v] == "W" :
                file.append(v)
                #trace_arete(s,v,'k',3)
                visited[v] = "G"
                ajouter_arete(laby,s,v)
        visited[s] = "K"
        #plt.pause(0.3)
        #trace_visite(visited)
    return laby
#         
# 
# #Animation (parcours en largeur)
# #plt.figure("largeur")
# 
# # trace_graphe(G,'r',.5)
# # laby = parcours_profondeur(G,(4,4))
# # trace_graphe(laby,'k',2)
# # plt.show()
# 