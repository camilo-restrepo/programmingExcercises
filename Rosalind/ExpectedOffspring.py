import numpy
import itertools

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

#Devuelve las combinaciones posibles del cruce de dos genotipos g1 y g2
def darGenotipos(g1, g2):
	genotipos = []
	genotipos.append(g1[0]+g2[0])
	genotipos.append(g1[0]+g2[1])
	genotipos.append(g1[1]+g2[0])
	genotipos.append(g1[1]+g2[1])
	return genotipos

#Devuelve la cuenta de cada genotipo en un cruce de dos genotipos
def contarGenotipos(g1, g2):
	genotipos = darGenotipos(g1, g2)
	dict = {}
	for i in genotipos:
		i = ordenarGenotipo(i)
		if dict.has_key(i):
			dict[i] = dict[i]+1
		else:
			dict[i] = 1
	return dict
		
def ordenarGenotipo(g):
	primera = g[0]
	segunda = g[1]
	if(primera.isupper()):
		return g
	else:
		return segunda+primera

#Meme que contarGenotipos pero devuelve probabilidades		
def darProbabilidadesGenotipos(g1, g2):
	dict = contarGenotipos(g1, g2)
	llaves = dict.keys()
	for i in llaves:
		dict[i] = dict[i]/4.0
	return dict

####################### FIN METODOS ADICIONALES ################

#VARIABLES DE LECTURA
# working_dir = '/Users/Pisco/Downloads/'
# input_file = working_dir+'rosalind_grph.txt'
# input = open(input_file, 'r')

#LEER ARCHIVO
# records = leerArchivoFASTA(input)
# input.close()

input = '19124 17895 19633 16451 16206 17835'
genotipos = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']

suma = 0
k=0
for i in genotipos:
	g1 = i.split('-')[0]
	g2 = i.split('-')[1]
	probs = darProbabilidadesGenotipos(g1, g2)
	probs_k = probs.keys()
	for j in probs_k:
		if j=='AA' or j=='Aa':
			suma = suma+(int(input.split(' ')[k])*(2*probs[j]))
	k=k+1

print suma
	



#VARIABLES DE ESCRITURA
# output_file = working_dir+'salida.txt'
# output = open(output_file, 'w')
# salida = ''

# output.write(salida.strip())
# output.close()
# print "DONE"
