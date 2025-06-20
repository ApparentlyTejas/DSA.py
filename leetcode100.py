class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def balanced(p , q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            
            return balanced(p.left , q.left) and balanced(p.right, q.right)
        return balanced(p , q)
    
# Time: O( n + m )
# Space: O( h )