import numpy as np

def cherche_centre(im):
    '''détermine le centre de gravité avec les formules du barycentre, utilisation des fonctions numpy pour réaliser la somme , im est l'image seuillée'''
    h=im.shape[0] #hauteur de l'image en pixels
    l=im.shape[1] #largeur de l'image en pixels
    im2D = im[:,:,0] #conversion de l'image : le contenu d'un pixel sera un nombre (ex : 1) au lieu d'une liste de 3 nombres identiques (ex : [1,1,1])
    
    sL=np.sum(im2D,0) #liste contenant la somme des lignes pour chaque colonne
    nC=np.arange(l) # liste contenant les indexs des colonnes : commence à zéro
    pos_p_x=sL*nC # liste contenant les positions pondérées
    
    sC=np.sum(im2D,1) #liste contenant la somme des colonnes pour chaque ligne
    nL=np.arange(h) #liste contenant les indexs des lignes 
    pos_p_y=sC*nL  #liste contenant les positions pondérées
    
    s=(np.sum(sL,0)) #somme de tous les éléments de la matrice
    
    if s>0: #calcul dans le cas où s n'est pas nul
        xg=np.sum(pos_p_x,0)/s #somme sur les colonnes des positions pondérées 
        yg=np.sum(pos_p_y,0)/s #somme sur les lignes des positions pondérées
    else: # si tous les pixels sont noirs, on place le cdg au centre de l'image
        xg=l/2
        yg=h/2
    return xg,yg