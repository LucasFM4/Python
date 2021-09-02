 n = 1
par = impar = 0
while n != 0:
	n = int(input('digite um valor: '))
	if n % 2 == 0:
		par += 1
	else:
		impar += 1
print('você digitou {} numeros pares e {} impares!'.format(par, impar))
