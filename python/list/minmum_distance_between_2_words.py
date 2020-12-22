class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
         dict_lst={}
         w1_p=-1
         w2_p=-1
         min_dist=100000000
         for v, k in enumerate(words):
             w1_p = v if k==word1 else w1_p
             w2_p = v if k==word2 else w2_p
             print (w1_p,w2_p)
             if w1_p!=-1 and w2_p!=-1 :
                min_dist=min(min_dist,(abs(w1_p-w2_p)))
         return min_dist
                
