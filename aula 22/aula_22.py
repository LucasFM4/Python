def fatorial(n):
	f = 1
	for c in range (1, n+1):
		f *= c
	return f


num = int(input('igite um Valor'))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}.')
