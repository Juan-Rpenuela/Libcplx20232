import math 
from math import sqrt
def suma (c1,c2) :
    """(input) ---> 2 tuplas las cuales primer elemento como numero real y el otro como su parte imaginaria
     se suma la parte real y por otro lado la parte imaginaria (OUTPUT)-----> COMPLEX NUMBER """
    parte_real  = c1[0]+c2[0]
    parte_i = c1[1]+c2[1]

    return (parte_real,parte_i)

def resta (c1,c2) :
    """(input) ---> 2 tuplas las cuales primer elemento como numero real y el otro como su parte imaginaria
     se resta la parte real y por otro lado la parte imaginaria (OUTPUT)-----> COMPLEX NUMBER """
    
    parte_real  = c1[0]-c2[0]
    parte_i = c1[1]-c2[1]

    return (parte_real,parte_i)
   
def multip(c1,c2):
    """(input) ---> 2 tuplas las cuales primer elemento como numero real y el otro como su parte imaginaria
     y multiplica como si fueran binomios de forma distributiva (OUTPUT)-----> COMPLEX NUMBER """
    
    parte_compleja = c1[0]*c2[0] + (-1*(c1[1]*c2[1]))
    parte_i = c1[0] * c2[1] + c2[0] * c1[1]

    return (parte_compleja,parte_i)
    
def conjugado(c1):
    """(input) ---> 1 tuplas la cual el primer elemento como numero real y el otro como su parte imaginaria
    se hallara el conjugado de este cambiando el signo de la parte imaginaria (OUTPUT)-----> COMPLEX NUMBER """
    c1 = list(c1)
    c1[1]=-1*c1[1]
    c1 = tuple(c1)
    return c1

def division (c1,c2):
    """(input) ---> 2 tuplas las cuales primer elemento como numero real y el otro como su parte imaginaria
     y DIVIDE multiplicando por el conjugado del denominador (OUTPUT)-----> COMPLEX NUMBER """
    numerador = multip(c1,conjugado(c2))
    denominador = multip(c2,conjugado(c2))
    parte_real = numerador[0]/denominador[0]
    parte_i = numerador[1]/denominador[0]
    return  (parte_real,parte_i)

def modulo (c1):
    """(input) ---> 1 tuplas la cual el primer elemento como numero real y el otro como su parte imaginaria
    se hallara el modulo haciendo teorema de pitagoras entre el imaginario y el real (OUTPUT)-----> COMPLEX NUMBER """
    mod = sqrt(c1[1]**2+c1[0]**2)
    return mod

def fase(c1):
    """(input) ---> 1 tuplas la cual el primer elemento como numero real y el otro como su parte imaginaria
    se hallara la fase (el angulo) (OUTPUT)-----> Entero """
    
    f = math.atan2(c1[1],c1[0])
    return f

def Pol_carte (c1):
    """(input) ---> 1 tupla la cual el primer elemento como numero real y el otro como un angulo
    a (OUTPUT)----->Tuple """
    parte_r = c1[0]*(math.cos(c1[1]))
    parte_i = c1[0]*(math.sin(c1[1]))
    return (parte_r,parte_i)


def carte_polar (c1):
    """(input) ---> 1 tuplas la cual el primer elemento como numero real y el otro como su parte imaginaria
    se hallara la fase (el angulo) 
    a coordenadas polares (OUTPUT)----->Tuple """
    parteC = modulo (c1)
    parte_i =  fase(c1)
    return ((parteC),parte_i)
