def largestAnagramSubstring(s): 
      
    # Returns total number of anagram 
    # substrings in s 

    n = len(s) 
    mp = dict() 
      
    # loop for length of substring 
    for i in range(n): 
        sb = '' 
        for j in range(i, n): 
            sb = ''.join(sorted(sb + s[j])) 
            print ('sb is ',sb)
            mp[sb] = mp.get(sb, 0) 
              
            # increase count corresponding 
            # to this dict array 
            mp[sb] += 1
  
    anas = 0
    max_k=''
    print ('mp is',mp)
    # loop over all different dictionary  
    # items and aggregate substring count 
    for k, v in mp.items(): 
        anas =max(anas,v)
        print ('anas ,',anas)
        if anas>=2 and len(k) > len(max_k):
            max_k=k
    return max_k
# Driver Code 
s = "xyxx"
print(largestAnagramSubstring(s)) 