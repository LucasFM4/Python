galera = list()
dado = list()
for c in range (0, 3):
	dado.append(str(input('Nome: ')))
	dado.append(str(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()
