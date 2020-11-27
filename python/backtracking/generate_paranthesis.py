class Solution(object):

    def generateParenthesis(self, n: int):
        result = []
        openCounter = 0
        closedCounter = 0
        self.generateValue(result, openCounter, closedCounter, n, "")
        return result

    def generateValue(self, result, openCounter, closedCounter, n, temp_str):
        if len(temp_str) == 2*n:
            result.append(temp_str)
            return
        if openCounter < n:
            self.generateValue(result, openCounter+1, closedCounter, n, temp_str+"(")
        if closedCounter < openCounter:
            self.generateValue(result, openCounter, closedCounter+1, n, temp_str+")")
