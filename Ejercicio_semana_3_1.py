# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:18:16 2019

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
##############################
#Gaussian Symplectic Ensemble (GSE)

n = 100#Dimensión de las matrices
s=int(n)
simul =10000 #Número de simulaciones

mat_eig = np.zeros((simul,n*2))

for i in range(1,simul+1) :

    #Creamos la matriz Herm
    a = np.random.normal(0,np.sqrt(1),(s, s)) + 1.j * np.random.normal(0,np.sqrt(1),(s, s))
    b = np.random.normal(0,np.sqrt(1),(s, s)) + 1.j * np.random.normal(0,np.sqrt(1),(s, s))
    H = np.concatenate(( np.concatenate((a,b), axis=1) ,np.concatenate ((-np.conj(b), np.conj(a)), axis=1) ), axis=0)
    H = (H + H.T.conj())/2
    #print(H)
    #Hasta aquí, todo bien 
    eig_val = LA.eigh(H)[0]
    mat_eig[i-1] = eig_val

gse = mat_eig.flatten()   
gse = (1/np.sqrt(4*n))*gse
 
plt.hist(gse, density=True)
#%%
#Gaussian Unitary Ensemble (GUE)

mat_eig = np.zeros((simul,n))

for i in range(1,simul+1) :

    #Creamos la matriz Herm
    H = np.random.normal(0,np.sqrt(1),(n, n)) + 1.j * np.random.normal(0,np.sqrt(1),(n, n))
    H = (H + H.T)/2
    #print(H)
    #Hasta aquí, todo bien 
    eig_val = LA.eigh(H)[0]
    mat_eig[i-1] = eig_val

gue = mat_eig.flatten()    
gue = (1/np.sqrt(2*n))*gue
plt.hist(gue, density=True)

#%%
#Gaussian Orthogonal Ensemble (GOE)

mat_eig = np.zeros((simul,n))

for i in range(1,simul+1) :

    #Creamos la matriz Herm
    H = np.random.normal(0,np.sqrt(1),(n, n)) 
    H = (H + H.T)/2
    #print(H)
    #Hasta aquí, todo bien 
    eig_val = LA.eig(H)[0]
    mat_eig[i-1] = eig_val

goe = mat_eig.flatten()   
goe = (1/np.sqrt(n))*goe 
plt.hist(goe, density=True)

#%%

indice = np.linspace(-np.sqrt(2),np.sqrt(2),num=1000)

indice = np.linspace(-2,2,num=10000)

circ = (1/np.pi)*np.sqrt(2-indice**2)

plt.plot(indice,circ)
#%%
fig_30, ax = plt.subplots()

e_gse = sns.distplot(gse, hist = False, kde = True,label="GSE")
e_gue = sns.distplot(gue, hist = False, kde = True,label="GUE")
e_goe = sns.distplot(goe, hist = False, kde = True,label="GOE")
circu = plt.plot(indice,circ,label="semi-círculo")
plt.title("Histograma de diferentes ensembles")
plt.legend(loc='upper right', frameon=False)
plt.show()

fig_30.savefig("ensembles.pdf", bbox_inches='tight') 














