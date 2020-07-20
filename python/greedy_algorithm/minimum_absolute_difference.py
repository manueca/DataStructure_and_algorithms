def minimumAbsoluteDifference(arr):
    n=len(arr)
    for i in range(0,len(arr)-1):
        for j in range(n - i - 1):
            if abs(arr[j])>abs(arr[j+1]):
                arr[j],arr[j+1]=abs(arr[j+1]),abs(arr[j])

    diff=10*200000

    if n < 2 or n > 10000 or arr[n-1]>(10**9):
        diff=0
    else:
    	diffs = []
    	for i in range(len(arr)-1):
        	diffs.append(abs(arr[i]-arr[i+1]))
    	return min(diffs)


if __name__ == '__main__':
	arr=[1,-3,71,68,17]
	print (minimumAbsoluteDifference(arr))

