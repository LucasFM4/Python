def contador(i, f, p):
	"""
	-> Faz uma contagem e mostra natela.
	:param i: inicio da contagem
	:param f: fim da contagem
	:param p: passo da contagem
	:return: sem retorno
	"""
	c = 1
	while c <= f:
		print(f'{c} ', end='')
		c += p
	print('fim!')


help(contador)
