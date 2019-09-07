# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:26:26 2019

@author: chiqu
"""

#Importamos librerías
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math  as mt
import seaborn as sns; sns.set()
from sklearn import preprocessing
import os

#%%

###########
# Cambiamos la dirección de trabajo
###########

os.getcwd()
os.chdir("C:\\Users\\chiqu\\Documents\\Lupita\\Maestria_Computo_Estadistico\\3er_Semestre\\3er_Semestre\\Selectos_Estadistica\\Notas clase\\Tarea Semana 3")

#%%
#Graficamos conjetura

indice = np.linspace(0,5,num=10000)

conj = (np.pi*indice/2)*np.exp(-np.pi*indice**2/4)

plt.plot(indice,conj)
#%%
# Segunda Versión
n = 100#Dimensión de las matrices
simul =1000

mat_eig = np.zeros((simul,n-1))

for i in range(1,simul+1) :

    #Creamos la matriz Herm
    H = np.random.normal(0,1,(n, n))    
    H = (H + H.T)/2
    #print(H)
    #Hasta aquí, todo bien 
    eig_val = LA.eig(H)[0]
    eig_val = np.sort(eig_val)[::-1] #ordena de mayor a menor
    
    s = eig_val[:-1]-eig_val[1:]
    mat_eig[i-1] = s

S = mat_eig.flatten()  
S = (1/np.mean(S))*S #ajustamos el valor de las S

#%%

fig_30, ax = plt.subplots()

plt.hist(S,density=True,bins=25)
plt.plot(indice,conj)
plt.show()

fig_30.savefig("Wigner.pdf", bbox_inches='tight') 


