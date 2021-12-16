estado = dict()
brasil = list()
for c in range(0, 3):
	estado['uf'] = str(input('Unidade Federativa'))
	estado['sigla'] = str(input('Sigla Do Estado'))
	brasil.append(estado.copy)
print(brasil)
