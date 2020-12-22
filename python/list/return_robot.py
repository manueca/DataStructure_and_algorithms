class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        a=0 
        b=0
        dir=0 # 0 N ,1 W , 2 S ,3 E
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in instructions:
            
            if i =='G':
                a+=directions[dir][0]
                b+=directions[dir][1]
            elif i == 'L':
                if dir==0 :
                    dir = 3 
                else:
                    dir-=1
                
            elif i == 'R':
                dir=(dir+1)%4
        print ('a,b,dir',a,b,dir)
        if (a==0 and b==0)  or dir !=0 :
            return True
        
        return False
