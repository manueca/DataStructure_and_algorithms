class Solution:
    def findSubStrings(self,s:str) -> list:
        uniq_set={}
        for i in range(len(s)):
            temp=""
            for j in range(i,len(s)):
                temp+=s[j]
                uniq_set[temp]=len(temp)
        return uniq_set
            
            
    def lastSubstring(self, s: str) -> str:
        dic=self.findSubStrings(s)
        print (dic)
        max_val=''
        for i in dic.keys():      
            print ('before',i,max_val)
            if i > max_val:
                max_val=i
            print ('after',i,max_val)
        return max_val
