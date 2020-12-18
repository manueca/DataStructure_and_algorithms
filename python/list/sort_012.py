def sort012 (arr, arr_size):
	high=arr_size-1
	mid=0
	low=0
	while mid <= high:
		if mid == 0:
	   		arr[mid],arr[low]=arr[low],arr[mid]
	   		low+=1
			mid+=1
		elif mid == 1:
	   		mid+=1
		else:
	   		arr[mid],arr[high]=arr[high],arr[mid]
	   		high+=1
	return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
arr_size = len(arr) 
arr = sort012( arr, arr_size) 
printArray(arr) 
