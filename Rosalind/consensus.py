import numpy

####################### METODOS ADICIONALES ################
class FastaRecord(object):
	def __init__(self, title, sequence):
		self.title = title
		self.sequence = sequence

def leerArchivoFASTA(input):
	results = []
	header = ''
	seq_items = []
	first = True
	for line in input:
		if line[0] == ';':
			continue # comment
		elif line[0] == '>':
			if not first:
				seq= "".join(seq_items)
				results.append(FastaRecord(header,seq))
				seq_items = []
			header = line[1:-1] # eat '>' and '\n'
			first = False
		else:
			seq_items.append(line[:-1])
	if len(seq_items) > 0:
		seq = "".join(seq_items)
		results.append(FastaRecord(header,seq))
	return results
	
def imprimir(records):
	for i in records:
		print i.sequence

####################### FIN METODOS ADICIONALES ################

#VARIABLES DE LECTURA
working_dir = '/Users/Pisco/Downloads/'
input_file = working_dir+'prueba.txt'
input = open(input_file, 'r')

#LEER ARCHIVO
records = leerArchivoFASTA(input)
input.close()

letras1 = {0:'A', 1:'C', 2:'G', 3:'T'}
letras = {'A':0, 'C':1,'G':2,'T':3}

matriz = numpy.zeros(shape=(4, len(records[0].sequence)))

for i in range(len(records)):
	registro = records[i]
	for j in range(len(registro.sequence)):
		base = registro.sequence[j]
		matriz[letras[base]][j] = matriz[letras[base]][j] +1

consensus = ''
for i in range(len(records[0].sequence)):
	max = 0
	indice = 0
	for j in range(4):
		if matriz[j][i]>max:
			max = matriz[j][i]
			indice = j
	consensus=consensus+letras1[indice]

#VARIABLES DE ESCRITURA
output_file = working_dir+'salida.txt'
output = open(output_file, 'w')
output.write(consensus+'\n')

r = matriz.tolist()
salida = ''
for i in range(4):
	text = letras1[i]+': '
	for j in range(len(records[0].sequence)):
		text = text + str(int(r[i][j]))+ ' '
	salida = salida + text.strip()+'\n'
output.write(salida.strip())
output.close()
print "DONE"
