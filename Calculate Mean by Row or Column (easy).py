def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode =='column':
		means=[]
	
		for j in range(len(matrix[0])):
			k=0
			for i in range(len(matrix)):
				k += matrix[i][j]
			k=k/len(matrix)
			means.append(k)
	else:
		means=[]
		for i in range(len(matrix)):
			k=0
			for j in range(len(matrix[0])):
				k += matrix[i][j]
			k=k/len(matrix[0])
			means.append(k)
			
	return means