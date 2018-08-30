#a = [ [1, 2, 4, 0], [3, -0.1, -0.2, 7.85], [2, 6, 0, 2]]
a = [ [1, 2, 4, 0, 1], [3, -0.1, -0.2, 7.85, 5], [2, 6, 0, 2, 3], [10, 6, 0, 2, 3]]

per = 2
suma=[]

def sumar():
	i=0
	for n in a:
		suma.append(0)
		#print('suma : ', suma)
		for x in range(len(n)-1):
			suma[i] = suma[i] + n[x]

		print(n)
		print('suma ', i+1, ' = ', suma[i])
		i = i + 1

def acomodar():
	
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i][j] > suma[i] - a[i][j]:
				print(a[i])
				print(a[i][j], ' es el mayor')
				aux = a[i]
				a[i] = a[j]
				a[j] = aux
				# if i==0:
				# 	print('Primero')
				# 	if j != 0:
				# 		aux=a[j]
				# 		a[j]=a[0]
				# 		a[0]=aux
	
		
def imprimirMatrizIndices():
	print('\n** MATRIZ **\n')
	o=0
	p=0
	for o in range(len(a)):
		for p in range(len(a)+1):
			print(a[o][p])
			p = p + 1
		print()
		o = p + 1
	print('\n\n')

def imprimirMatriz():
	print('\n** MATRIZ **\n')
	for n in a:
		print(n)
	print('\n\n')

imprimirMatriz()
sumar()
acomodar()

imprimirMatriz()


#print( 'x[i]  = ( ' ,n[len(n)-1], ' - ', n[len(n)-3], ' * ',  x[i+1], ' - ', n[len(n)-2], ' * ', x[i+2], ' )  / ',  n[i], ' )')
#x[i] = (n[len(n)-1] - n[len(n)-3] * x[i+1] - n[len(n)-2] * x[i+2]) / n[i]
#print('x1 = ', x[0] )
#	Error = (xi^j - xi^j-1) / xi^j
