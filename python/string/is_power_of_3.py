class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        else:
            print ('before while')
            while (n % 3 == 0):
                print (n)
                n /= 3   
            print (n)
            return n == 1
