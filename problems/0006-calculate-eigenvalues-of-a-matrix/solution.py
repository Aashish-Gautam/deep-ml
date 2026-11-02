import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace=0
	for r,row in enumerate(matrix):
		trace+=row[r]
	det=np.linalg.det(np.array(matrix))
	lambda1=(trace+(trace**2-4*det)**0.5)/2
	lambda2=(trace-(trace**2-4*det)**0.5)/2
	return [lambda1,lambda2]