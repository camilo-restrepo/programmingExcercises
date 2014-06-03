import numpy
import itertools
import math
import urllib
import re
from sets import Set

####################### METODOS ADICIONALES #######################
class FastaRecord(object):
	def __init__(self, title, sequence):
		self.title = title
		self.sequence = sequence

def readFASTAFile(input):
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
genetic_code = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I',
	'GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V',
	'UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S',
	'CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y','CAU':'H',
	'AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D','UAA':'Stop','CAA':'Q','AAA':'K',
	'GAA':'E','UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R','AGU':'S','GGU':'G',
	'UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G','UGG':'W',
	'CGG':'R','AGG':'R','GGG':'G'}
	
def ARN2AA(sequence):
	result = ''
	i = 0
	while i<len(sequence):
		if i+3<=len(sequence):
			triplet = sequence[i:i+3]
			result = result+genetic_code[triplet]
		i=i+3
	return result
	
def ADN2ARN(sequence):
	return sequence.replace('T', 'U')
	
def ADN2AA(sequence):
	return ARN2AA(ADN2ARN(sequence))
	
def isStopCodon(codon):
	return genetic_code[codon]=='Stop'
	
def kMersLexicographically(alfabeto, number):
	resultList = list(itertools.product(alfabeto, repeat=number))
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
	
def hammingDistance(sequence1, sequence2):
	return sum(ch1 != ch2 for ch1, ch2 in zip(sequence1, sequence2))
	
def transitionTransversionRatio(sequence1, sequence2):
	transitions=0
	transversions=0
	for i in range(len(sequence2)):
		b1 = sequence1[i]
		b2 = sequence2[i]	
		#Si la mutacion es transition
		if (
				(b1=='A' and b2=='G') or (b1=='G' and b2=='A') 
				or (b1=='C' and b2=='T') or (b1=='T' and b2=='C')
			):
			transitions=transitions+1
		else:
			#si es transversion
			if (
					(b1=='A' and b2=='C') or (b1=='C' and b2=='A') 
					or (b1=='G' and b2=='T') or (b1=='T' and b2=='G')
					or (b1=='A' and b2=='T') or (b1=='T' and b2=='A')
					or (b1=='C' and b2=='G') or (b1=='G' and b2=='C')
				):
				transversions = transversions+1

	return float(transitions)/float(transversions)

#Devuelve ORF de una cadena  de ARN desde una posicion de inicio
#Devuelve la cadena desde una posicion de inicio hasta un codon Stop
def getORF(sequencia, inicio):
	i=inicio
	tamanio = len(sequencia)
	cadena = ''
	hayStart = False
	while i < tamanio:
		codon = sequencia[i:i+3]
		if codon == 'AUG':
			cadena = cadena + codon
			hayStart = True
		elif hayStart and not isStopCodon(codon):
			cadena = cadena + codon
		if isStopCodon(codon):
			return ARN2AA(cadena)
		i=i+3

#Devuelve todas las ORFs posibles en una cadena de ADN sin repetidos
def getAllORFS(sequencia):
	seq = ADN2ARN(sequencia)
	i=0
	tamanio = len(seq)
	result = []
	while i < tamanio:
		if i+3 < tamanio:
			codon = seq[i:i+3]
			if codon == 'AUG':
				salida = getORF(seq, i)
				if salida != None:
					result.append(salida)
		i = i+1

	seq = sequencia
	seq = ADN2ARN(getReverseComplement(seq))
	i=0
	while i < tamanio:
		if i+3 < tamanio:
			codon = seq[i:i+3]
			if codon == 'AUG':
				salida = getORF(seq, i)
				if salida != None:
					result.append(salida)
		i = i+1
	return Set(result)
	

def getReverseComplement(sequencia):
	complementos = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	result = ''
	sequencia = sequencia[::-1]
	for i in sequencia:
		result = result + complementos[i]
	return result
			
####################### FIN METODOS BIOINFORMATICA #######################


#VARIABLES DE LECTURA
working_dir = '/Users/Pisco/Downloads/'
input_file = working_dir+'rosalind_orf.txt'
input = open(input_file, 'r')

#LEER ARCHIVO
records = readFASTAFile(input)
input.close()

seq = records[0].sequence
s = getAllORFS(seq)
for x in s:
	print x


#VARIABLES DE ESCRITURA
# output_file = working_dir+'salida.txt'
# output = open(output_file, 'w')
# salida = ''

# output.write(salida.strip())
# output.close()
# print "DONE"
