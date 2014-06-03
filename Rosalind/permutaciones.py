input = '6'
n = int(input)
lista = []
for i in range(n):
	lista.append(i+1)

result = list(itertools.permutations(lista))
salida=''
for i in result:
	for j in i:
		salida = salida + str(j) + ' '
	salida = salida.strip()
	salida=salida+'\n'

print len(result)
print salida.strip()
