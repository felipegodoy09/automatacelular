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

def celular(ini,patron):
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
	mostrar(temp)
	return temp

mostrar(prueba)
aux = celular(prueba,patron30)
for i in range(20):
	aux = celular(aux,patron30)



