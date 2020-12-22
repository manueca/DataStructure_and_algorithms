class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        s_list=list(s)
        max_val = ""
        substr=[]
        for i in range(n,-1,-1):
            max_val=max(max_val,''.join(s[i:]))        
        return max_val
