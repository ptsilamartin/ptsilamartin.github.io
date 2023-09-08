# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:19:55 2022

@author: xpess
"""
##Exercice 1

def mult_it(n, p):
    ''' Réalise le produit n * p , de manière itérative '''
    prod = 0
    for i in range (p):
        prod = prod + n
    return(prod)

def mult_rec(n, p):
    ''' Réalise le produit n * p , de manière récursive '''
    if p == 0:
        return 0
    else :
        return mult_rec(n,p-1) + n

##Exercice 2

def Wallis_it(n :int):
    """ renvoie une valeur approchée du nombre pi, méthode de Wallis itérative """
    p=2
    for i in range (1,n+1):
        p=p*(4*i**2)/(4*i**2-1)
    return(p)

#>>> Wallis_it(10)
#3.0677038066434976

def Wallis_rec(n :int):
    """ renvoie une valeur approchée du nombre pi, méthode de Wallis itérative """
    if n==0:
        return(2)
    else:
        return(Wallis_rec(n-1)*((4*n**2)/(4*n**2-1)))
#>>> Wallis_rec(10)
#3.0677038066434985

def Gregory_it(n :int):
    """ renvoie une valeur approchée du nombre pi, méthode de Gregory itérative """
    s=0
    for i in range (0,n+1):
        s=s+(-1)**i/(2*i+1)
    return(4*s)

#>>> Gregory_it(10)
#3.232315809405594

def Gregory_rec(n :int):
    """ renvoie une valeur approchée du nombre pi, méthode de Gregory recursive """
    if n==0:
        return(1*4)
    else:
        return(Gregory_rec(n-1)+(-1)**n/(2*n+1)*4 )

#>>> Gregory_rec(10)
#3.232315809405594


##Exercice 3

def miroir_rec(mot):
    """ fonction récursive retournant le miroir d'une chaîne de caractères """
    n=len(mot)
    if len(mot) <= 1:
        return mot
    else:
        return miroir_rec(mot[1:])+mot[0]
#>>> miroir_rec("Eh! çà va la vache !")
#'! ehcav al av àç !hE'


def est_palindrome(mot):
    """ fonction recursive indiquant si la chaine de caractère mot est un palindrome, les espaces sont ignorés"""
    if len(mot)<=2 :
        return (mot[0]==mot[-1])
    else:
        if mot[0]!=mot[-1]:
            return(False)
        else :
            return est_palindrome(mot[1:-1])


##Exercice 4
def fibonacci_it(n):
    """fibonacci itérative"""
    a=0
    b=1
    for i in range(n-1): # invariant en entrée : a=u_i, b=u_{i+1}
        c=a+b
        a=b
        b=c
        # invariant en sortie : a=u_{i+1}, b=u_{i+2}
    return (b) # à la fin de la boucle, i=n-2

##Exercice 5
def fibonacci_rec(n):
    """fibonacci recursive avec renvoi de u_n"""
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonacci_rec(n-1)+fibonacci_rec(n-2))

def fibonacci_rec2(n):
    """fibonacci recursive avec renvoi de deux valeurs de u_n"""
    if n==0:
        return (0,1)
    elif n==1:
        return (1,1)
    else:
        X = fibonacci_rec2(n-1)
        return (X[1],X[0]+X[1])



def numerote(x, y):
    if x == 0 and y == 0:
        return 0
    if y > 0:
        return 1 + numerote(x+1, y-1)
    return 1 + numerote(0, x-1)

def reciproque(n):
    if n == 0:
        return (0, 0)
    (x, y) = reciproque(n-1)
    if x > 0:
        return (x-1, y+1)
    return (y+1, 0)

##Exercie 6 : Flocons
#matrice rotation d'angle pi/3
import numpy as np
import matplotlib.pyplot as plt
def rotation(angle):
    return np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])

# angle=np.pi/3
# print (rotation(angle))

def koch(a, b, n):
    R = rotation(np.pi/3)
    if n == 0:
        plt.plot([a[0], b[0]], [a[1], b[1]],'b')
    else:
        c=np.array([(b[0]-a[0])/3+a[0],(b[1]-a[1])/3+a[1]])
        d=np.array([2*(b[0]-a[0])/3+a[0],2*(b[1]-a[1])/3+a[1]])
        vecteur=d-c
        e=np.dot(rotation(np.pi/3),vecteur)+c
        koch(a, c, n - 1)
        koch(c, e, n - 1)
        koch(e, d, n - 1)
        koch(d, b, n - 1)

def flocon(a,b,n):
    koch(a,b,n)
    vecteur=b-a
    c=np.dot(rotation(-2*np.pi/3),vecteur)+b
    koch(b,c,n)
    koch(c,a,n)

# n = 5
# a = np.array([0,0])
# b = np.array([1,0])
# flocon(a, b, n)
# plt.axis('equal')
# plt.show()