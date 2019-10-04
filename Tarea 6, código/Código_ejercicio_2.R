############################################################
# Ejercicio 2, inciso a
############################################################
p0=4 #tenemos 4 variables

n0=48 # observaciones de todas las pob

k0=6 # las poblaciones

p=p0

m=n0-k0

n= k0-1

#teta(p,n-k,k-1) bajo la nula tiene esta distrib

fi = 2*asin(sqrt( (max(p,n)-.5)/(m+n-1) ))

gama = 2*asin(sqrt( (min(p,n)-.5)/(m+n-1) ))

mu = 2*log(tan( (gama+fi)/2) )

c = sin(gama)*sin(fi)*sin(gama+fi)^2  

Sigma = ( (16/47^2)*(1/c) )^(1/3)

f1_05 = qtw(0.95, beta=1, log = FALSE)

teta_05= exp(mu+f1_05*Sigma)/ (1+exp(mu+f1_05*Sigma) )

mu
Sigma
f1_05
teta_05

################################################
#Ejercicio 2, inciso b
################################################


library(heplots)
library(RMTstat)

data(RootStock)


#Vamos a quitar 4 obs de cada grupo
roots <- RootStock[5:44,]
roots <- roots[-c(9:12),]
roots <- roots[-c(25:28),]
roots <- roots[-c(17:20),]
roots <- roots[-c(9:12),]

table(roots$rootstock)#Verificamos que nos quedemos sólo con 4 observaciones
#

#Hacemos MANOVA en la forma convencional
manRes1 <- manova(cbind(girth4, ext4, girth15, weight15) ~ rootstock, data=roots)

summary(manRes1, test="Wilks") #sacamos la lambda de wilks
#con el p valor que resulta, vemos que rechazamos la nula

summary(manRes1, test="Roy") # obtenemos el estadístico de Roy
# con el p valor que resulta, vemos que rechazamos la nula

resultado <- summary(manRes1, test="Roy") #Lo que da como Roy es el lambda más alto
3.4707/4.4707#el estadístico de Roy

resultado$Eigenvalues #obtenemos los eigenvalores, vemos que el más grande es 3.47(este es nuestro lambda observad)

#para hacer tracy widom, necesito calcular el estadístico tracy y también el lambda máximo observado

############################################################
# Sacamos el test tracy widom
############################################################
library(RMTstat)

p0=4 #tenemos 4 variables

n0=24 # observaciones de todas las pob

k0=6 # las poblaciones

p=p0

m=n0-k0

n= k0-1

#teta(p,n-k,k-1) bajo la nula tiene esta distrib

fi = 2*asin(sqrt( (max(p,n)-.5)/(m+n-1) ))

gama = 2*asin(sqrt( (min(p,n)-.5)/(m+n-1) ))

mu = 2*log(tan( (gama+fi)/2) )

c = sin(gama)*sin(fi)*sin(gama+fi)^2  

Sigma = ( (16/47^2)*(1/c) )^(1/3)

f1_05 = qtw(0.95, beta=1, log = FALSE)

teta_05= exp(mu+f1_05*Sigma)/ (1+exp(mu+f1_05*Sigma) )

mu
Sigma
f1_05
teta_05


