import math as m

def f_pseudo(tom0,z):
    return 1-((math.exp(-z*tom0))/(math.sqrt(1-z*z)))*math.sin(tom0*math.sqrt(1-z*z)+math.asin(math.sqrt(1-z*z)))

    
def f_aperiodique(tom0,z):
    return 1+(math.exp(-tom0*(z+math.sqrt(z*z-1))))/(2*(z*math.sqrt(z*z-1)+z*z-1))-(math.exp(-tom0*(z-math.sqrt(z*z-1))))/(2*(z*math.sqrt(z*z-1)-z*z+1))
    
def f_critique(tom0):
    """
    Fonction permettant de calculer s(tom0) dans le cas ou z>1. 
    Entrées :
        * tom0, flt : le temps réduit - sans unité
    Sortie : 
        * res, flt : s(tom0) - ici, sans unité.
    """


def f_s(tom0,z):
    """
    Fonction permettant de calculer la réponse indicielle d'un système du second ordre. 
    Entrées : 
        * tom0, flt : temps de réponse réduit
        * z, flt : coefficient d'amortissement
    Sortie : 
        * s(tom0,z), flt
    """



def is_in_strip(x):
    """
    Fonction permettant de savoir si une valeur est dans la bande des + ou - 5% de la valeur finale.
    Entrée : 
        x, flt : réel
    Sortie : 
        True si la valeur est dans la bande à + ou - 5%
        False si la valeur n'est pas dans la bande à + ou - 5%
    """


def calcul_tom0(z,tom0=500):
    """
    Recherche du temps de réponse à 5%
    Entrées : 
       * z, flt : coefficient d'amortissement
       * tom0 (flt, optionnel) : si non précisé, on calcule le temps de réponse en partant de tom0 = 500
    Sortie : 
       * tom0 (flt) : temps de réponse à 5%
    """
    pas_tom0=0.05
    x = f_s(tom0,z) 
    if z<0.7:
        # Dans cas, s'assurer que le tom0 initial est suffisamment grand
        while is_in_strip(x) :
            tom0  = tom0 - pas_tom0
            x = f_s(tom0,z)
        tom0=tom0+pas_tom0
    else :
        # Dans cas, s'assurer que le tom0 initial est suffisamment petit
        while not is_in_strip(x) :
            tom0  = tom0 + pas_tom0 
            x = f_s(tom0,z)
        tom0=tom0-pas_tom0
    return tom0



def make_xy()
    xx,yy = [],[]
    n = 1000
    z = 0.01
    tom0 = 500
    pasz = 0.01
    while z<=100:
        print(z)
        if z<0.7:
            tom0=calcul_tom0(z,tom0)
        else :
            tom0=calcul_tom0(z,0)
      
        if z<0.1:
            pasz = 0.001
        elif z<1:
            pasz = 0.01
        elif z<10:
            pasz = 0.1
        else :
            pasz = 1
        
        xx.append(z)
        yy.append(tom0)
        z=z+pasz
    return xx,yy



def plot_abaque(xx,yy):
    plt.plot(xx,yy,label="Temps de réponse réduit $tr \\omega_0$")
    plt.xlabel("Coefficient d'amortissement $\\xi$")
    plt.ylabel("Temps de réponse réduit $tr \\omega_0$")
    plt.title("Temps de réponse réduit d'un système du 2nd ordre")
    plt.legend()
    plt.loglog()
    plt.grid(which="major",axis="x",linewidth=1.5, linestyle='-')
    plt.grid(which="major",axis="y",linewidth=1.5, linestyle='-')
    plt.grid(which="minor",axis="x",linewidth=0.75, linestyle='-', color='0.75')
    plt.grid(which="minor",axis="y",linewidth=0.75, linestyle='-', color='0.75')

