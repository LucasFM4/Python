teste = list()
teste.append('Bom Dia')
teste.append('Lucas')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'Davi'
teste[0] = 23
galera.append(teste[:])
print(galera)
