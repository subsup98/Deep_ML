def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b=[[]for _ in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[0])):
			b[j].append(a[i][j])
	return b