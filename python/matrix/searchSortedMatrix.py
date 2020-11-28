def searchInSortedMatrix(matrix, target):
    # Write your code here.
	result=[-1,-1]
	result_flg=0
	for i in range(len(matrix)):
		for j in range(len(matrix)+1):
			print (i,j,matrix[i][j])
			result_flg=1 if matrix[i][j] == target else 0  if matrix[i][j]<target  else 2
			if result_flg==1:
				return [i,j]
			elif result_flg==2:
				break
			else:
				continue
	return result
		
	

