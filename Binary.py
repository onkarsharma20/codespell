#python3 code for binary tree if it is height balanced or not

class Solution:
    def checklr(self,root):
        if root==None:
            return 0
        h1= self.checklr(root.left)
        h2= self.checklr(root.right)
        
   
        if h1!=-1 and h2!=-1:
            if abs(h1-h2)>1:
                return -1
            else:
                return 1+max(h1,h2)
        else:
            return -1
        
    def isBalanced(self,root):
        #add code here
        if self.checklr(root)==-1:
            return False
        else:
            return True
