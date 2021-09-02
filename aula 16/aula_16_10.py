galera = list()
dado = list()
totmai = totmen = 0
for c in range (0, 3):
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()

for p in galera:
	if p[1] >= 21:
		print('{p[0]} é maior de Idade.')
	else:
		print('{p[0]} é maior de Idade.')
