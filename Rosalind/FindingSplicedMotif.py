import numpy
import itertools
import math

####################### METODOS ADICIONALES #######################
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
		
####################### FIN METODOS ADICIONALES #######################

####################### METODOS PROBABILIDAD #######################

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
	
#Pone la primera en mayuscula
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
	
####################### FIN METODOS PROBABILIDAD #######################

####################### METODOS BIOINFORMATICA #######################

def traducirARN2AA(sequence):
	genetic_code = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I',
	'GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V',
	'UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S',
	'CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y','CAU':'H',
	'AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D','UAA':'Stop','CAA':'Q','AAA':'K',
	'GAA':'E','UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R','AGU':'S','GGU':'G',
	'UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G','UGG':'W',
	'CGG':'R','AGG':'R','GGG':'G'}
	
	result = ''
	i = 0
	while i<len(sequence):
		if i+3<len(sequence):
			triplet = sequence[i:i+3]
			result = result+genetic_code[triplet]
		i=i+3
	return result
	
def traducirADN2ARN(sequence):
	return sequence.replace('T', 'U')
	
def traducirADN2AA(sequence):
	return traducirARN2AA(traducirADN2ARN(sequence))
	
def kMersLexicographically(str, number):
	resultList = list(itertools.product(str, repeat=number))
	result = []
	for i in resultList:
		result_str = ''
		for j in range(len(i)):
			result_str = result_str+i[j]
		result.append(result_str)
	return result
	
def GCContent(sequence):
	cont_gc=0.0
	for char in sequence:
		if char=='C' or char=='G':
			cont_gc=cont_gc+1
	result = (cont_gc/len(sequence))*100
	return result

####################### FIN METODOS BIOINFORMATICA #######################


#VARIABLES DE LECTURA
working_dir = '/Users/Pisco/Downloads/'
input_file = working_dir+'rosalind_sseq.txt'
input = open(input_file, 'r')

#LEER ARCHIVO
records = leerArchivoFASTA(input)
input.close()

seq = records[0].sequence
result=''
last_index = 0
cadena = records[1].sequence
for i in range(len(cadena)):
	letra = cadena[i]
	agrego = 0
	for j in range(len(seq)):
		if seq[j]==letra and j>last_index+1 and agrego==0:
			result=result+' '+str(j+1)
			last_index = j
			agrego=1

print result
			



#VARIABLES DE ESCRITURA
# output_file = working_dir+'salida.txt'
# output = open(output_file, 'w')
# salida = ''

# output.write(salida.strip())
# output.close()
# print "DONE"
