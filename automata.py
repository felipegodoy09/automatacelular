from tkinter import *

inicial = [0,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0]
prueba =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
patron110 = [	['000',0],
				['001',1],
				['010',1],
				['011',0],
				['100',1],
				['101',0],
				['110',0],
				['111',1]]

patron30 = 	[	['000',0],
				['001',1],
				['010',1],
				['011',1],
				['100',1],
				['101',0],
				['110',0],
				['111',0]]

def mostrar(lista):
	for i in lista:
		print(i,end="")
	print()

def buscar(s,ptr):
	for i in range(len(ptr)):
		if(s == ptr[i][0]):
			return ptr[i][1]

def lista_to_string(lista):
	temp = ""
	for i in lista:
		temp = temp + str(i)
	return temp

def dibujar_matriz(n,m,matriz,tam=10):
	for i in range(n):
		for j in range(m):
			if(matriz[j][i]== 0):
				cuadrado = areaDibujo.create_rectangle((2+i*tam),(2+j*tam),(tam+2+i*tam),(tam+2+j*tam),fill = "white")
			elif(matriz[j][i]==1):
				cuadrado = areaDibujo.create_rectangle((2+i*tam),(2+j*tam),(tam+2+i*tam),(tam+2+j*tam),fill = "black")

def un_celular(ini,patron):
	temp = []
	l= len(ini)
	s = str(ini[-1]) + str(ini[0]) + str(ini[1])
	temp.append(buscar(s,patron))
	i = 0
	while (len(temp)<l):
		if(i == l-1):
			s = str(ini[i]) + str(ini[0]) + str(ini[1])
		elif(i == l-2):
			s = str(ini[i]) + str(ini[i+1]) + str(ini[0])
		else:
			s = str(ini[i]) + str(ini[i+1]) + str(ini[i+2])
		i=i+1
		if(i==l):
			i=0
		temp.append(buscar(s,patron))
		#a = s + " -> " + str(buscar(s,patron30))
		
		#print(a)
	#mostrar(temp)
	return temp

def celular_n(ini,n,patron):
	matriz = []
	matriz.append(ini)
	#mostrar(prueba)
	aux = un_celular(ini,patron)
	matriz.append(aux)
	for i in range(n):
		aux = un_celular(aux,patron)
		matriz.append(aux)
	return matriz


m = celular_n(prueba,21,patron30)
n = len(prueba)
k = len(m)
ventana = Tk()											#constructor,se inicia script de interfaz grafica
areaDibujo = Canvas(ventana,width=800,height=800)		#constructor, se inicia area de dibujo
ventana.geometry("800x800")								#tamaño de la ventana
areaDibujo.place(x=10,y=10)								#se posiciona area de dibujo
ventana.title("Automata Celular")						#titulo de ventana
dibujar_matriz(n,k,m)									#ejecuta funcion de dibujo
ventana.mainloop()										#finaliza e inicia la interfaz
