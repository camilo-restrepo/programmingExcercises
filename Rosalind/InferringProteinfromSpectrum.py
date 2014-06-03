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
	
def reverseGeneticCode():
	inv = {}
	for k in genetic_code.keys():
		valor = genetic_code[k]
		vals = []
		if valor in inv:
			vals = inv[valor]
			vals.append(k)
			inv[valor] = vals
		else:
			vals.append(k)
			inv[valor] = vals
		
	return inv
	
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
	
#Devuelve el reverse complement de una cadena de adn
def getReverseComplement(sequencia):
	complementos = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	result = ''
	sequencia = sequencia[::-1]
	for i in sequencia:
		result = result + complementos[i]
	return result

#Longest common substring entre de una lista de strings
def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr
#Metodo adicional para long_substr
def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

#Longest common subsequence entre dos cadenas
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = str(a[x-1])+ " " + result
            x -= 1
            y -= 1
    return result

#Devuelve longest increasing subsequence de un arreglo de numeros
def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        #  such that seq[M[j]] < seq[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]    # reversing

#Longest decreasing subsequence
def LDS( A ):
	m = [0] * len( A ) # starting with m = [1] * len( A ) is not necessary
	for x in range( len( A ) - 2, -1, -1 ):
		for y in range( len( A ) - 1, x, -1 ):
			if m[x] <= m[y] and A[x] > A[y]:
				m[x] = m[y] + 1 # or use m[x]+=1
	max_value = max( m )
	result = []
	for i in range( len( m ) ):
		if max_value == m[i]:
			result.append( A[i] )
			max_value -= 1
 
  	return result

#Edit Distance between two strings
def editDistance(seq1, seq2):
	m = len(seq1)
	n = len(seq2)
	i=0
	v = numpy.zeros(shape=(m+1,n+1))
	while i <= m:
		v[i][0] = i
		i=i+1
	j=0
	while j <= n:
		v[0][j] = j
		j=j+1
	i=1
	j=1
	while i <= m:
		j=1
		while j <= n:
			if seq1[i-1] == seq2[j-1]:
				v[i][j]=v[i-1][j-1]
			else:
				v[i][j]=1+min(v[i-1][j], v[i][j-1], v[i-1][j-1])
			j=j+1
		i=i+1
	return int(v[m][n])
	
#Computes Knuth-Morris-Pratt (KMP) algorithm table 
def kpm_table(word):
	T = []
	i = 0 
 	while i <= len(word):
 		T.append(0)
 		i=i+1
 
	pos=2
	cnd=0
	while pos < len(word):
		if word[pos-1]==word[cnd]:
			cnd=cnd+1
			T[pos] = cnd
			pos = pos + 1
		elif cnd>0:
			cnd=T[cnd]
		else:
			T[pos] = 0
			pos = pos+1
	return T

monoisotopic_table = {
"A":71.03711,
"C":103.00919,
"D":115.02694,
"E":129.04259,
"F":147.06841,
"G":57.02146,
"H":137.05891,
"I":113.08406,
"K":128.09496,
"L":113.08406,
"M":131.04049,
"N":114.04293,
"P":97.05276,
"Q":128.05858,
"R":156.10111,
"S":87.03203,
"T":101.04768,
"V":99.06841,
"W":186.07931,
"Y":163.06333 }

####################### FIN METODOS BIOINFORMATICA #######################


#VARIABLES DE LECTURA
working_dir = '/Users/Pisco/Downloads/'
input_file = working_dir+'rosalind_spec.txt'
input = open(input_file, 'r')

#LEER ARCHIVO
# records = readFASTAFile(input)
# input.close()
lineas = input.readlines()
input.close()

i=0
vals = []
result = ''
reverse_table = {v:k for k, v in monoisotopic_table.items()}

while i < len(lineas)-1:
	val = float(lineas[i].strip())
	next = float(lineas[i+1].strip())
	
	for k in reverse_table:
# 		print str(val+k)+' ' + str(next)+' '+ str(round(val+k, 4) == round(next, 4))
		if round(val+k, 4) == round(next, 4):
			result = result + reverse_table[k]
			break
	i = i+1

print result
print str(len(result))+ ' '+str(len(lineas))
	

# ordenado = []
# for i in data:
# 	ordenado.append(i)
# ordenado.sort()
# ordenado = ordenado[::-1]
# print len(lcs(data, ordenado))


#VARIABLES DE ESCRITURA
# output_file = working_dir+'salida.txt'
# output = open(output_file, 'w')
# salida = ''

# output.write(salida.strip())
# output.close()
# print "DONE"
