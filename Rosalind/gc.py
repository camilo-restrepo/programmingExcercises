working_dir = '/Users/Pisco/Downloads/'
input_file = working_dir+'rosalind_prot.txt'
#output_file = working_dir+''
input = open(input_file, 'r')
#output = open(output_file, 'w')
archivo = input.readlines()

for str in archivo:
	str = str.strip()
	if str[0]=='>' or str==archivo[-1]:
		if str==archivo[-1]:
			cadena = cadena + str
		#CALCULO GC
		if len(cadena) > 0:
			cont_gc=0.0
			for char in cadena:
				if char=='C' or char=='G':
					cont_gc=cont_gc+1
			result = (cont_gc/len(cadena))*100
			result = round(result, 6)
			if(result>val_max):
				val_max=result
				label_max=label[1:]
		#FIN CALCULO GC
		label = str
		cadena = ''
	else:
		cadena = cadena + str

print label_max
print('%.6f' % round(val_max,6))
#output.close()
input.close()
