class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir=0
        left=0 
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        
        ret=[]
        while (top<=bottom and left<=right):
            if dir==0:
                print ('left,right',left,right)
                for i in range(left,right+1):
                    ret.append(matrix[left][i])
                top+=1
            
                print ("left,right,dir,ret : 0 ",left,right,dir,ret)
                
            elif dir==1:
                
                for i in range(top,bottom+1):
                    
                    ret.append(matrix[i][right])
                
                right-=1
                print ("top,bottom,dir,ret : 1 ",top,bottom,dir,ret)
                
            elif dir==2:
                for i in range(right,left-1,-1):
                    
                    ret.append(matrix[bottom][i])
                    
                bottom-=1    
                
                print ("right,left,dir,ret : 2 ",right,left,dir,ret)
                
            
            elif dir==3:
                
                for i in range (bottom,top-1,-1):
                    ret.append(matrix[i][left])
                left+=1
                
                print ("top,bottom,dir,ret : 3 ",bottom,top,dir,ret)
                
            print ('dir is ',dir,left)
            dir=((dir+1)%4)
            
        
        return ret
