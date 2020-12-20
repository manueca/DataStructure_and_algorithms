# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,res,flag):
        if root is None:
            return None
        if not flag: res.append(root.val)
        if root.right and root.left:
            self.dfs(root.right,res,True)
            self.dfs(root.left,res,True)
        elif root.right:
            self.dfs(root.right,res,False)
        elif root.left:
            self.dfs(root.left,res,False)
            
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        res=[]
        self.dfs(root,res,True)
        return res