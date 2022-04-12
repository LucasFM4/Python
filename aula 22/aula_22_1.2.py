def contador(i, f, p):
	c = 1
	while c <= f:
		print(f'{c}', end='')
		c += p
	print('fim!')


contador(2, 10, 2)
