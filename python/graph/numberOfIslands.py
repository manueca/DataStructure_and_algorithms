class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        print (rows,cols)
        islands=0
        isVisited=set()
        def dfs(r,c):
            if ( (r not in range (rows)
                or c not in range (cols))
                or grid[r][c]=="0"
                or (r,c) in isVisited
                ):
                return 
            
            isVisited.add((r,c))
            print ("outside  loop",r,c)
            direction_list=[[1,0],[-1,0],[0,1],[0,-1]]
            for rd,cd in direction_list:
                print ("inside loop",r,c,r+rd,r+cd)
                dfs(r+rd,c+cd)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in isVisited:
          
                    islands+=1
                    dfs(r,c)
        
        return islands
