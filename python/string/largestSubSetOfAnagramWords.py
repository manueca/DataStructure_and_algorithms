def largestAnagramSubstring(s): 
      
    # Returns total number of anagram 
    # substrings in s 

    n = len(s) 
    mp = dict() 
    s_list=s.split()

    # loop for length of substring 
    for i in s_list: 
        print ('i is ',i)
        sb = ''.join(sorted(i))
        print ('sb is ',sb)
        mp[sb] = mp.get(sb, 0) 
        mp[sb] += 1
  
    anas = 0
    max_k=''
    print ('mp is',mp)
    # loop over all different dictionary  
    # items and aggregate substring count a
    for k, v in mp.items(): 
        anas =max(anas,v)
        print ('anas ,',anas)
        if anas>=2 and len(k) > len(max_k):
            max_k=k
    return max_k
# Driver Code 
s = "ant magenta magnate tan gnamate"
print(largestAnagramSubstring(s)) 