"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
"""

class Solution:
  def findLongestWord(self, s: str, d: list[str]) :
     print (s,d)
     def check(s,s1):
          i=0
          j=0
          while(i<len(s) and j<len(s1)):
              if s[i]==s1[j]:
                  i=i+1
                  j=j+1
                  continue
              i=i+1
              
          return j==len(s1)
     res=""
     for word in d:
          if check(s,word) and (len(res)<len(word) or (len(res)==len(word) and res>word)):
              res=word
     return res

findLongestWord(self,"abpcplea",["ale","apple","monkey","plea"])
