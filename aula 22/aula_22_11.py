def contador(i, p):
	"""
	-> Faz uma contagem e mostra na tela.
	:param i: unicio de contagem
	:parem f:fimda contagem
	:param p: passo da contagem
	:return: sem retorno
	"""
	c = i
	while c <=f:
		print(f'{c} ',end='')
		c += p
		print('fim')


help(contador)
