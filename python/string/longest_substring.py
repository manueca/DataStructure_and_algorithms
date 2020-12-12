class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq_set={}
        start=0
        max_size=0
        for i in range(len(s)):
            print (s[i],uniq_set.keys())
            if s[i] not in uniq_set.keys():
                uniq_set[s[i]]=1
                print (uniq_set)
                if len(uniq_set)> max_size:
                    max_size=len(uniq_set)
            else:
                 print ('start is ',start,s[i],i)
                 while (s[start] != s[i]) :
                    print ('uniq_set is',uniq_set)
                    del uniq_set[s[start]]
                    start+=1
                    print ('start is ',start)
                
                 start+=1
        return max_size
