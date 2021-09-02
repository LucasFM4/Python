teste = list()
galera = list()
teste.append('Lucas')
teste.append(9)
print(teste)
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 22
print(teste)
galera.append(teste[:])
teste[0] = 'camila'
teste[1] = 20
print(teste)
galera.append(teste[:])

print(galera)
