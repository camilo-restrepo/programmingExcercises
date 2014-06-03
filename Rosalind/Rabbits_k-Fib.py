input = '30 5'
n = int(input.split(' ')[0])
k = int(input.split(' ')[1])

list = []
for i in range(n):
	list.append(0)

list[0] = 1
list[1] = 1
list[2] = 1+k
i=3
while i<n:
	list[i]=list[i-1]+list[i-2]*k
	i=i+1

print list[n-1]
