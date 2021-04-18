class Solution(object):

    def generateParenthesis(self, n: int):
        rowCounter = 0
        colCounter=0
        result = [[0 for i in range(n)] for j in range(n)] 
        self.generateValue(result, rowCounter, colCounter,n)
        return result
	
    def generateValue(self, result, rowCounter,colCounter,  n):
        if rowCounter <= n-1 and colCounter <= n-1:
           result[rowCounter][colCounter]='*'
        if rowCounter == n-1 and colCounter==n-1:
               return result
        if colCounter <= n-1 :
            self.generateValue(result, rowCounter,colCounter+1, n)
        if rowCounter < colCounter :
            colCounter=0
            self.generateValue(result, rowCounter+1,colCounter, n)
testInstance = Solution()
print(testInstance.generateParenthesis(5))
