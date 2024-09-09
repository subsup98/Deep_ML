def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c=[]
	if len(a[0]) != len(b):
		return -1
	for i in range (len(a)):
		k=0
		for j in range(len(b)):
			k +=a[i][j]*b[j]		
		c.append(k)
	
	return c
