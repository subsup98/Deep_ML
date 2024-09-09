![image](https://github.com/user-attachments/assets/6e3cf3aa-c223-429a-bb8b-911eee18128e)


def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c=[]
	if len(a[0]) < len(b):
		return -1
	for i in range (len(a)):
		k=0
		for j in range(len(b)):
			k +=a[i][j]*b[j]		
		c.append(k)
	
	return c
