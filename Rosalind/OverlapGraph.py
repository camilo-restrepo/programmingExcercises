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
	
def imprimirRecords(records):
	for i in records:
		print i.sequence
		
####################### FIN METODOS ADICIONALES ################

#VARIABLES DE LECTURA
working_dir = '/Users/Pisco/Downloads/'
input_file = working_dir+'rosalind_grph.txt'
input = open(input_file, 'r')

#LEER ARCHIVO
records = leerArchivoFASTA(input)
input.close()

k = 3
dict = {}

for r in records:
	adjacentes = []
	sufijo = r.sequence[-3:]
	for otro in records:
		if otro!=r:
			if otro.sequence.startswith(sufijo):
				adjacentes.append(otro.title)
	if r.title not in dict:
		dict[r.title] = adjacentes

#VARIABLES DE ESCRITURA
output_file = working_dir+'salida.txt'
output = open(output_file, 'w')
salida = ''
elems = dict.items()
for e in elems:
	for i in e[1]:
		salida = salida + e[0]+' '+i+'\n'
output.write(salida.strip())
output.close()
print "DONE"
