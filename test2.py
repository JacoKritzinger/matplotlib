A = []
B = []

with open('values.txt', 'r') as myfile:
	for line in myfile:
		Y.append( int(line) )

A = list(range(0,len(B)+1))
print(A)
print(B)