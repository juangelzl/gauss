a = [ [3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]]
#a = [ [1, 4, 2, 2], [1, 2, 4, 0], [4, 1, 2, 0]]
#a = [ [1, 2, 4, 0], [4, 1, 2, 0], [1, 4, 2, 2]]
#a = [ [1, 2, 4, 0, 1], [1, 0, 2, 4, 5], [2, 4, 0, 1, 3], [4, 1, 0, 2, 3]]
#a = [ [1, 2, 5, 0, 1, 0], [2, 5, 0, 1, 1, 0], [1, 0, 2, 5, 1, 0], [5, 1, 0, 2, 1, 0], [1, 1, 0, 2, 5, 0]]
#a = [ [1, 2, 6, 0, 1, 1, 0], [2, 1, 0, 1, 1, 6, 0], [2, 6, 0, 1, 1, 1, 0], [1, 0, 2, 6, 1, 1, 0], [6, 1, 0, 2, 1, 1, 0], [1, 1, 0, 2, 6, 1, 0]]
#a = [ [6, 1, 0, 2, 1, 1, 9], [2, 6, 0, 1, 1, 1, 8], [1, 2, 6, 0, 1, 1, 7], [1, 0, 2, 6, 1, 1, 6], [1, 1, 0, 2, 6, 1, 5], [2, 1, 0, 1, 1, 6, 4]]

per = 2
suma = []
r = []
for n in a:
	suma.append(0)
	r.append(0)
# def imprimirMatriz():
# 	for n in a:
# 		print(n)

def sumar():
	#print('\n** Sumar() **\n')
	i=0
	for n in a:
		suma[i] = 0
		#print('suma : ', suma)
		for x in range(len(n)-1):
			suma[i] = suma[i] + n[x]

		#print(n)
		#print('suma ', i+1, ' = ', suma[i])
		i = i + 1

def acomodar():
	m=0

	#print('\n** Acomodar() **\n')
	while m == 0:
		#print('\nwhile\n')
		for i in range(len(a)):
			sumar()
			#print('\n\n')
			#print(a[i])
			for j in range(len(a)):
			
				#print(a[i][j], ' > ', suma[i] - a[i][j])
				if a[i][j] > suma[i] - a[i][j]:
					#print(' si ')
					#print(a[i][j], ' es el mayor')
					if i!=j:
						print(' acomodar ', i + 1, ' en ', j + 1)
						aux = a[i]
						a[i] = a[j]
						a[j] = aux
						m=m+1
						imprimirMatriz()
						break
					else:
						m=m-1
						break
				#else:
					#print(' no ')

		
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
acomodar()

imprimirMatriz()

for i in range(len(a)):
	print('\n\nResultados\n', r)
	for k in range(len(a)):
		s = 0
		for j in range(len(a)):
			if j != i:
				print('a[',i,'][',j,  '] * ',  'r[',j,']')
				print(a[i][j],  ' * ',  r[j])
				s = s + a[i][j] * r[j]
				# print(a[j][i],  ' * ',  r[i])
				# s = s + a[j][i] * r[i]
		if i == k:
			r[i] = (a[i][len(a)] - s)/a[i][k]
			print('(',a[i][len(a)], ' - ', s,') / ', a[i][k], ' = ', r[i])
			

#print( 'x[i]  = ( ' ,n[len(n)-1], ' - ', n[len(n)-3], ' * ',  x[i+1], ' - ', n[len(n)-2], ' * ', x[i+2], ' )  / ',  n[i], ' )')
#x[i] = (n[len(n)-1] - n[len(n)-3] * x[i+1] - n[len(n)-2] * x[i+2]) / n[i]
print('\n\nResultados\n\n')
i=0
for res in r:
	print('x[',i,'] =', res)
	i=i+1


#print(' \n\n\n\n0 / 4 = ', 0/4)
#	Error = (xi^j - xi^j-1) / xi^j
