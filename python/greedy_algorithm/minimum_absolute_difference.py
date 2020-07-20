def minimumAbsoluteDifference(arr):
    n=len(arr)
    for i in range(0,len(arr)-1):
        for j in range(n - i - 1):
            if abs(arr[j])>abs(arr[j+1]):
                arr[j],arr[j+1]=abs(arr[j+1]),abs(arr[j])

    diff=10*20

    if n < 2 or n > 10000 or arr[n-1]>(10**9):
        diff=0
    else:
        for i in range(n-1): 
            print (arr[i],i)
            if abs(arr[i+1] - arr[i]) < diff: 
                diff =abs(arr[i+1] - arr[i])
                print (arr[i+1],arr[i],diff)
    return diff


if __name__ == '__main__':
	arr=[1,-3,71,68,17]
	print (minimumAbsoluteDifference(arr))

