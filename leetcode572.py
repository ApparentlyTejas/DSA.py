class Solution:
    def isSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p , q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return isSame(p.left , q.left) and isSame(p.right , q.right)

        def hasSubTree(root):
            if not root:
                return False

            if isSame(root , subRoot):
                return True
            
            return hasSubTree(root.left) or hasSubTree(root.right)
        
        return hasSubTree(root)
    
# Time: O(m * n)     
# Space: O(n)