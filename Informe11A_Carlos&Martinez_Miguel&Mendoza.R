# -*- coding: utf-8 -*-
"
Created on Mon Apr 23 2020

@author: Savuth S.
"

generador <- function(mn, mx, fl, cl) {
	ran_array <- array(dim = c(fl, cl))

	for (f in 1:fl) { 
		for (c in 1:cl) {
			ran_array[f,c] <- floor(runif(1,min=mn,max=mx))
		}
	}
	return (ran_array)
}

imprimir <- function(ar_2d, nm_fl, nm_cl){
	for (f in 1:4){
		print(paste("----", nm_fl[f], "----"),digits = 2, quote = FALSE)
		for (c in 1:12){
			print(paste("    ", nm_cl[c],": ", ar_2d[f,c], "M $COP"), digits = 2, quote = FALSE)
		}
	}
}

imprimir_personalizado <- function(ar_2d,mn, mx,nm_fl, nm_cl){
	for (f in 1:4){
		print(paste("----", nm_fl[f], "----"),digits = 2, quote = FALSE)
		for (c in mn:mx){
			print(paste("    ", nm_cl[c],": ", ar_2d[f,c], "M $COP"), digits = 2, quote = FALSE)
		}
	}
}

promedio <- function(br_ng, br_gr, br_gn, nm_fl=Names_Dictionary()){ 
	for (f in 1:4){
		print("\n--"+str(nm_fl[f])+"--")
		
		sum = 0
		for (c in 1:12){
			sum += br_ng[f,c]
			print(paste("Ingresos: ",sum/12,"M $COP"),digis = 2, quote = FALSE)
		}

		for (c in 1:12){
			sum += br_gr[f,c]
			print(paste("Egresos: ",sum/12,"M $COP"),digis = 2, quote = FALSE)
		}
		
		for (c in 1:12){
			sum += br_gn[f,c]
			print(paste("Ganancias: ",sum/12,"M $COP"),digis = 2, quote = FALSE)
		}
	}
}
  "Calcula el promedio de una fila de valores en tres array bidimensional"

#Checks
ar_tam = np.shape(br_ng)
if(ar_tam[0] != np.shape(br_gr)[0] or ar_tam[0] != np.shape(br_gn)[0]): #Simetria
  print("\n\nERROR: Los arrays son de tamaños diferentes\n\n")
return

#Ordanmiento de variables
np.sort(br_ng)
np.sort(br_gr)
np.sort(br_gn)

for f in range(0,ar_tam[0],1):
  print("\n--"+str(nm_fl[f])+"--")

sum = 0
for c in range(1,ar_tam[1]-1,1):
  sum += br_ng[f,c]
print("Ingresos: "+ str(round(sum/ar_tam[1],2))+"M $COP")

sum = 0
for c in range(1,np.shape(br_gr)[1]-1,1):
  sum += br_gr[f,c]
print("Egresos: "+ str(round(sum/np.shape(br_gr)[1],2))+"M $COP")

sum = 0
for c in range(1,np.shape(br_gn)[1]-1,1):
  sum += br_gn[f,c]
print("Ganancias: "+ str(round(sum/np.shape(br_gn)[1]-2,2))+"M $COP")     
}

restador <- function(br_mn,br_st){
	ar_resul <- array(dim = c(4,12))

	for (f in 1:4){
		for (c in 1:12){
			ar_resul[f,c] = br_mn[f,c]-br_st[f,c]
		}
	}
	return (ar_resul)
}

meses <- c("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
sucursales <- c("Buracamanga", "Floridablanca", "Girón", "Piedecuesta")
años <- c("2019", "2018", "2017", "2016", "2015")

ingresos <- generador(100,180,4,12)
egresos <- generador(60,130,4,12)
ganancias <- restador(ingresos,egresos)

print("~~~~Ingresos por sucursal en meses~~~~", quote = FALSE)
imprimir(ingresos, sucursales, meses)

print("~~~~Egresos por sucursal en meses~~~~", quote = FALSE)
imprimir(egresos, sucursales, meses)

print("~~~~Ganancias por sucursal en meses~~~~", quote = FALSE)
imprimir(ganancias, sucursales, meses)